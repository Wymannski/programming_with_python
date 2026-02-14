from unittest import TestCase
from matrix2Dim import Matrix2Dim, IncoherentException, IncorrectDimensionsException


class TestMatrix2Dim(TestCase):
    def setUp(self):
        self.matrix_symmetric = Matrix2Dim((3, 3), [[2, 1, 1], [1, 3, 1], [1, 1, 4]])

    def test_get_element_when_element_existing_should_return_element(self):
        value = 3
        self.assertEqual(self.matrix_symmetric.get_element(1, 1), value)

    def test_get_element_when_row_index_not_existing_should_throw_index_error(self):
        with self.assertRaisesRegex(IndexError,'row index out of bound'):
            self.matrix_symmetric.get_element(4, 1)

    def test_get_element_when_column_index_not_existing_should_throw_index_error(self):
        with self.assertRaisesRegex(IndexError,'column index out of bound'):
            self.matrix_symmetric.get_element(1, 3)

    def test_set_element_should_set_element_at_index(self):
        value = 1
        self.matrix_symmetric.set_element(0, 0, value)
        self.assertEqual(self.matrix_symmetric.get_element(0, 0), value)

    def test_set_element_when_row_index_not_existing_should_throw_index_error(self):
        with self.assertRaisesRegex(IndexError,'row index out of bound'):
            self.matrix_symmetric.set_element(4, 1, 0)

    def test_set_element_when_column_index_not_existing_should_throw_index_error(self):
        with self.assertRaisesRegex(IndexError,'column index out of bound'):
            self.matrix_symmetric.set_element(1, 3, 0)

    def test_transpose(self):
        transposed_matrix = Matrix2Dim((3,3),[[2,1,1],[1,3,1],[1,1,4]])
        self.assertEqual(self.matrix_symmetric.transpose(),transposed_matrix)

    def test_is_symmetric_when_is_symmetric_should_return_true(self):
        self.assertTrue(self.matrix_symmetric.is_symmetric())

    def test_is_symmetric_when_dimensions_are_not_equal_should_return_false(self):
        matrix = Matrix2Dim((2,3))
        self.assertFalse(matrix.is_symmetric())

    def test_is_symmetric_when_elements_are_not_symmetric_should_return_false(self):
        matrix = Matrix2Dim((3,3),[[0,0,0],[1,0,0],[0,0,0]])
        self.assertFalse(matrix.is_symmetric())

    def test_total(self):
        total = 15
        self.assertEqual(self.matrix_symmetric.total(),total)

    def test_total_when_1x1_matrix(self):
        matrix = Matrix2Dim((1,1),[[1]])
        total = 1
        self.assertEqual(matrix.total(),total)

    def test_average(self):
        decimal_place = 1
        average = 1.66
        self.assertAlmostEqual(self.matrix_symmetric.average(),average,decimal_place)

    def test_average_when_1x1_matrix(self):
        matrix = Matrix2Dim((1,1),[[1]])
        average = 1
        self.assertEqual(matrix.average(),average)

    def test_is_coherent_when_coherent_should_return_true(self):
        self.assertTrue(self.matrix_symmetric.is_coherent())

    def test_init_when_incoherent_should_return_throw_incoherent_exception(self):
        with self.assertRaises(IncoherentException):
            Matrix2Dim((2,1),[[1],[1,1]])

    def test_init_when_row_count_0_should_return_throw_dimensions_exception(self):
        with self.assertRaises(IncorrectDimensionsException):
            Matrix2Dim((0, 1))

    def test_init_when_column_count_0_should_return_throw_dimensions_exception(self):
        with self.assertRaises(IncorrectDimensionsException):
            Matrix2Dim((1, 0))

    def test_eq_when_equal_should_return_true(self):
        matrix = Matrix2Dim((3, 3), [[2, 1, 1], [1, 3, 1], [1, 1, 4]])
        self.assertTrue(self.matrix_symmetric == matrix)

    def test_eq_when_not_equal_should_return_false(self):
        matrix = Matrix2Dim((3, 3), [[1, 1, 1], [1, 3, 1], [1, 1, 4]])
        self.assertFalse(self.matrix_symmetric == matrix)

    def test_str(self):
        result = "(3, 3)\n|2||1||1|\n|1||3||1|\n|1||1||4|\n"
        self.assertEqual(str(self.matrix_symmetric),result.lstrip())

