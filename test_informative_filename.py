import unittest
import parse_filename as pf



testfile = pf.informative_filename("filename.png")

#This is a test suite to see if the remove extension method works
# class test_remove_extension(unittest.TestCase):
#     def test_extension_removal_basic(self):
#         # teststring = remove_extension("filename.png")
#         testfile.original_filename = "filename.png"
#         self.assertEqual("filename", testfile.remove_extension())
#     def test_extension_removal_with_multiple_periods(self):
#         testfile.original_filename = "file3.6.png"
#         self.assertEqual("file3.6", testfile.remove_extension())
#     def test_extension_removal_only_extension(self):
#         testfile.original_filename = ".png"
#         self.assertEqual("", testfile.remove_extension())
#     def test_extension_removal_other_extension(self):
#         testfile.original_filename = "file.jpg"
#         self.assertEqual("file", testfile.remove_extension())
#     def test_extension_removal_short_extension(self):
#         testfile.original_filename = "file.pn"
#         self.assertEqual("file", testfile.remove_extension())
#     def test_extension_removal_long_extension(self):
#         testfile.original_filename = "file.pngjndkg"
#         self.assertEqual("file", testfile.remove_extension())
#     def test_extension_removal_no_extension(self):
#         testfile.original_filename = "file"
#         self.assertEqual("file", testfile.remove_extension())
#     def test_extension_removal_even_more_periods(self):
#         testfile.original_filename = "exposure3_UV2.5_B3.2.png"
#         self.assertEqual("exposure3_UV2.5_B3.2", testfile.remove_extension())
#     def test_extension_removal_even_more_values(self):
#         testfile.original_filename = "exposure3_UV2.5838_B3.2884.png"
#         self.assertEqual("exposure3_UV2.5838_B3.2884", testfile.remove_extension())
#     def test_extension_removal_periods_without_numbers(self):
#         testfile.original_filename = "exp.pos.ure.html"
#         self.assertEqual("exp.pos.ure", testfile.remove_extension())

#This is a test suite for the informatice filename class to determine whether it extracts the slice num, and the voltages correctly
class test_extract_information(unittest.TestCase):

    # def test_extract_info_basic(self):
    #     testfile = pf.informative_filename("Exposure3_UV2.3_B2.2")
    #     testfile.extract_voltage()
    #     self.assertEqual(3, testfile.slice_num)
    #     self.assertEqual(2.3, testfile.UV_voltage)
    #     self.assertEqual(2.2, testfile.blue_voltage)
    def test_extract_info_diff(self):
        testfile = pf.informative_filename("Exposure3_UV2_B2_T1")
        # testfile.extract_voltage()
        self.assertEqual(3, testfile.information_list[0])
        self.assertEqual(2, testfile.information_list[1])
        self.assertEqual(2, testfile.information_list[2])
    def test_extract_info_class(self):
        testfile = pf.informative_filename("Exposure3_UV2_B2_T2.5.png")
        self.assertEqual(3, testfile.slice_num)
        self.assertEqual(2, testfile.UV_voltage)
        self.assertEqual(2, testfile.blue_voltage)
        self.assertEqual(2.5, testfile.display_time)
    def test_extract_info_class_more_complex(self):
        testfile = pf.informative_filename("Exposure3_UV2.46_B2.86_T0.016.png")
        self.assertEqual(3, testfile.slice_num)
        self.assertEqual(2.46, testfile.UV_voltage)
        self.assertEqual(2.86, testfile.blue_voltage)
        self.assertEqual(0.016, testfile.display_time)
    def test_extract_info_class_multidigit_numbers(self):
        testfile = pf.informative_filename("Exposure3_UV12.46_B82.86_T0.006.png")
        self.assertEqual(3, testfile.slice_num)
        self.assertEqual(12.46, testfile.UV_voltage)
        self.assertEqual(82.86, testfile.blue_voltage)
        self.assertEqual(0.006, testfile.display_time)
    def test_extract_info_time(self):
        testfile = pf.informative_filename("Exposure3_UV12.46_B82.86_T2.15.png")
        self.assertEqual(3, testfile.slice_num)
        self.assertEqual(12.46, testfile.UV_voltage)
        self.assertEqual(82.86, testfile.blue_voltage)
        self.assertEqual(2.15, testfile.display_time)

# class test_read_files(unittest.TestCase):

#     def test_read_in(self):
#         # 
#         IMAGE_PATH = "Users/vishwanathan/Documents/UM-1/undergrad_research/microfabrication/mf_test_slices"
#         newlist = pf.readfiles(IMAGE_PATH)
#         for file in newlist:
#             print


if __name__ == '__main__':

    unittest.main()