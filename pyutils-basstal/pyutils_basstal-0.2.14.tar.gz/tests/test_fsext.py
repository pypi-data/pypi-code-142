import shutil
import time
import unittest
import pyutils.fsext as fs
import os


class TestFsext(unittest.TestCase):

    def setUp(self) -> None:
        self.test_root_dir = os.path.dirname(__file__)
        return super().setUp()

    def tearDown(self) -> None:
        target_dir = os.path.join(self.test_root_dir, 'sync_data')
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)

        target_dir = os.path.join(self.test_root_dir, 'sync_data1')
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        return super().tearDown()

    def test_to_base64(self):
        cwd = os.getcwd()
        if not cwd.endswith('tests'):
            os.chdir('tests')
        self.assertEqual(fs.to_base64('abs'), '')
        self.assertNotEqual(fs.to_base64('./data/to_base64.png'), '')
        output_dir = './output'
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        os.makedirs(output_dir)
        output_file = os.path.join(output_dir, 'to_base64')
        content = fs.to_base64('./data/to_base64.png', output_file)
        with open(output_file, 'r+', encoding='utf-8') as f:
            self.assertEqual(f.readline(), content)

    def test_convert_encoding(self):
        with open(os.path.join(self.test_root_dir, 'data/test_convert_encoding'), 'rb') as f:
            test_convert_encoding = f.read()
        gbk_encoding_source_path = os.path.join(self.test_root_dir, "data/gbk_encoding")
        test_gbk_encoding_path = os.path.join(os.path.dirname(gbk_encoding_source_path), 'test_gbk_encoding')
        shutil.copyfile(gbk_encoding_source_path, test_gbk_encoding_path)
        with open(test_gbk_encoding_path, 'rb') as f:
            gbk_encoding = f.read()
        self.assertNotEqual(gbk_encoding, test_convert_encoding)
        fs.convert_encoding(test_gbk_encoding_path)
        with open(test_gbk_encoding_path, 'rb') as f:
            gbk_encoding = f.read()
        self.assertEqual(gbk_encoding, test_convert_encoding)

    def test_copy_files(self):
        """copy_files 将目标文件列表中的文件复制到目标文件夹下，目标文件列表可以包含文件或文件夹。
        """
        # 测试 copy 简单的文件 和 文件夹
        target_path = os.path.join(self.test_root_dir, 'data/copy_test')
        source_dir = os.path.join(target_path, 'source')
        source_list = [os.path.join(source_dir, filename) for filename in os.listdir(source_dir)]

        fs.copy_files(target_path, source_list)
        filenames = [filename for filename in os.listdir(source_dir)]
        for filename in filenames:
            self.assertTrue(os.path.exists(os.path.join(target_path, filename)))

        # 测试 覆盖 的效果
        test_copy_file_path = os.path.join(target_path, 'test_copy_file')
        with open(test_copy_file_path, 'w+') as f:
            f.write('add more info')
        fs.copy_files(target_path, source_list)
        with open(test_copy_file_path, 'r+') as f:
            lines = f.readlines()
        content = '\n'.join(lines)
        self.assertTrue('add more info' not in content)

    def test_get_dirs(self):
        """get_dirs 获得指定目录下所有文件夹
        """
        target_path = os.path.join(self.test_root_dir, 'data/get_dirs')
        result_dirs = fs.get_dirs(target_path, ignore_patterns=['**/.svn'])
        self.assertTrue(len(result_dirs) == 1)
        result_dirs = fs.get_dirs(target_path)
        self.assertTrue(len(result_dirs) == 2)
        result_dirs = fs.get_dirs(target_path, recursive=True)
        self.assertTrue(len(result_dirs) == 4)

    def test_sync_folder(self):
        """sync_folder 同步两个目录内的内容
        """
        src_path = os.path.join(self.test_root_dir, 'data')
        target_path = os.path.join(self.test_root_dir, 'sync_data')
        # sync_folder simple
        files = fs.get_files(src_path, ['*.py'])
        sync_result = fs.sync_folder(src_path, target_path, files)
        self.assertTrue(sync_result)
        tmp_py = os.path.join(target_path, 'tmp.py')
        with open(tmp_py, 'w') as f:
            f.write('print("hello")')
        target_files = fs.get_files(target_path, ['*.py'])
        another_target_path = os.path.join(self.test_root_dir, 'sync_data1')
        sync_result = fs.sync_folder(target_path, another_target_path, target_files)
        self.assertTrue(sync_result)
        # sync_folder with remove_diff
        os.remove(tmp_py)
        sync_result = fs.sync_folder(target_path, another_target_path, target_files, remove_diff=True)
        self.assertTrue(sync_result)
        self.assertFalse(os.path.exists(os.path.join(another_target_path, 'tmp.py')))
        time.sleep(0.1)
        from pathlib import Path
        src_touch_py = os.path.join(src_path, 'touch_me.py')
        Path(src_touch_py).touch()
        sync_result = fs.sync_folder(src_path, another_target_path, files, remove_diff=True)
        self.assertTrue(sync_result)
        another_target_touch_py = os.path.join(another_target_path, 'touch_me.py')
        target_touch_py = os.path.join(target_path, 'touch_me.py')
        self.assertTrue(os.path.getmtime(another_target_touch_py) - os.path.getmtime(target_touch_py) > 1)
        self.assertTrue(os.path.getmtime(src_touch_py) - os.path.getmtime(another_target_touch_py) <= 1)
        sync_result = fs.sync_folder(target_path, another_target_path, target_files, remove_diff=True, compare_content=True)
        self.assertFalse(sync_result)
        with open(target_touch_py, 'a') as f:
            f.write('\n# add something new')
        sync_result = fs.sync_folder(target_path, another_target_path, target_files, remove_diff=True, compare_content=True)
        self.assertTrue(sync_result)
        with open(target_touch_py, 'r') as f:
            target_touch_content = ''.join(f.readlines())
        with open(another_target_touch_py, 'r') as f:
            another_target_touch_content = ''.join(f.readlines())
        self.assertEqual(target_touch_content, another_target_touch_content)
        sync_result = fs.sync_folder(target_path, another_target_path, target_files, remove_diff=True, compare_content=True, remove_original=True)
        self.assertTrue(sync_result)
        self.assertFalse(os.path.exists(target_touch_py))

        files = fs.get_dirs(src_path, True)
        sync_result = fs.sync_folder(src_path, target_path, files, remove_diff=True)
        self.assertTrue(sync_result)
