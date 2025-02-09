import unittest
import microfabrication_functions as pf



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
        self.assertEqual(3, testfile.slice_num)
        self.assertEqual(2, testfile.UV_voltage)
        self.assertEqual(2, testfile.blue_voltage)
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
    def test_extract_info_change_values(self):
        testfile = pf.informative_filename("Exposure3_UV12.46_B82.86_T0.006.png")
        self.assertEqual(3, testfile.slice_num)
        self.assertEqual(12.46, testfile.UV_voltage)

    def test_extract_info_change_filename(self):
        testfile = pf.informative_filename("Exposure3_UV12.46_B82.86_T0.006.png")
        self.assertEqual(3, testfile.slice_num)
        self.assertEqual(12.46, testfile.UV_voltage)
        self.assertEqual(82.86, testfile.blue_voltage)
        self.assertEqual(0.006, testfile.display_time)
        testfile.original_filename = "Exposure2_UV1.86_B2.86_T0.15.png"
        self.assertEqual(2, testfile.slice_num)
        self.assertEqual(1.86, testfile.UV_voltage)
        self.assertEqual(2.86, testfile.blue_voltage)
        self.assertEqual(0.15, testfile.display_time)
    def test_minimal_filename(self):
        testfile.original_filename = "2_1.86_2.86_0.15.png"
        self.assertEqual(2, testfile.slice_num)
        self.assertEqual(1.86, testfile.UV_voltage)
        self.assertEqual(2.86, testfile.blue_voltage)
        self.assertEqual(0.15, testfile.display_time)
    def test_missing_values(self):
        testfile.original_filename = "2_2.86_0.15.png"
        self.assertEqual(2, testfile.slice_num)
        self.assertEqual(2.86, testfile.UV_voltage)
        self.assertEqual(0.15, testfile.blue_voltage)
        self.assertEqual(0, testfile.display_time)
    def test_empty_string(self):
        testfile.original_filename = ""
        self.assertEqual(0, testfile.slice_num)
        self.assertEqual(0, testfile.UV_voltage)
        self.assertEqual(0, testfile.blue_voltage)
        self.assertEqual(0, testfile.display_time)
    def test_missing_singular(self):
        testfile.original_filename = "2_x_2.86_0.15.png"
        self.assertEqual(2, testfile.slice_num)
        self.assertEqual(0, testfile.UV_voltage)
        self.assertEqual(2.86, testfile.blue_voltage)
        self.assertEqual(0.15, testfile.display_time)
        

class test_read_files(unittest.TestCase):

    def test_read_in(self):
        IMAGE_PATH = "/Users/vishwanathan/Documents/UM-1/undergrad_research/microfabrication/mf_test_slices"
        newlist = pf.read_files(IMAGE_PATH)
        for file in newlist:
            print(file)
        print('\n')
    def test_read_in_parse(self):
        IMAGE_PATH = "/Users/vishwanathan/Documents/UM-1/undergrad_research/microfabrication/mf_test_slices"
        newlist = pf.read_files(IMAGE_PATH)
        for file in newlist:
            print('{} {} {} {}'.format(file.slice_num, file.UV_voltage, file.blue_voltage, file.display_time))
        print('\n')
    def test_read_in_manipulate(self):
        IMAGE_PATH = "/Users/vishwanathan/Documents/UM-1/undergrad_research/microfabrication/mf_test_slices"
        newlist = pf.read_files(IMAGE_PATH)
        for file in newlist:
            print(file.slice_num+ file.UV_voltage+ file.blue_voltage+ file.display_time)
        self.assertEqual(newlist[0].slice_num, 1)
        print('\n')
class test_write_files(unittest.TestCase):
    
    def insert_at_end(self, num, orig_str):
        future_index = len(orig_str)
        for index, x in enumerate(orig_str):
            if (x.isdigit()):
                future_index=index
                break
        new_str = orig_str[0:future_index]+ str(num)
        return new_str 
    def test_insert_at_end_basic(self):
        self.assertEqual(self.insert_at_end(2.4, "exposure1.3"), "exposure2.4")
    def test_insert_at_end_no_numbers(self):
        self.assertEqual(self.insert_at_end(1.8, "exposure"), "exposure1.8")
    def test_insert_at_end_no_numbers_again(self):
        self.assertEqual(self.insert_at_end(1.8, "num"), "num1.8")
    def test_insert_at_end_numbers(self):
        self.assertEqual(self.insert_at_end(1.8, "num2.7867"), "num1.8")
    def test_rewrite_filename_basic(self):
        new_testfile = pf.informative_filename("Exposure1_UV3.2_B2.2.png")
        new_file = new_testfile.insert_new_data(2, new_testfile.original_filename, "slice_num", ".png" )
        self.assertEqual(new_file, "Exposure2_UV3.2_B2.2.png" )

        

if __name__ == '__main__':

    unittest.main()