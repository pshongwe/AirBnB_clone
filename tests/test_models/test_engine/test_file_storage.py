#!/usr/bin/python3
"""File storage tests"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """File Storage Unit tests class"""

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_initial_state(self):
        """Initial state"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_new_and_all(self):
        """test new and all"""
        user = User()
        user.id = 12345
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {'User.12345': user})

    def test_save_and_reload(self):
        """test save and reload"""
        user = User()
        user.id = 12345
        self.storage.new(user)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(new_storage.all(), {'User.12345': user})

    def test_get_object_by_id(self):
        """test get object by id"""
        user = User()
        user.id = 12345
        self.storage.new(user)
        self.assertEqual(self.storage.get_object_by_id("User", 12345), user)
        self.assertIsNone(self.storage.get_object_by_id("User", 54321))

    def test_delete(self):
        """ test delete"""
        user = User()
        user.id = 12345
        self.storage.new(user)
        self.storage.delete(user)
        self.assertIsNone(self.storage.get_object_by_id("User", 12345))

    def test_reload_no_file(self):
        """test reload no file"""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_invalid_json(self):
        """test reload invalid json"""
        with open("file.json", "w") as f:
            f.write("invalid_json")
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_empty_json(self):
        """test reload empty json"""
        with open("file.json", "w") as f:
            f.write("{}")
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_valid_json_with_unknown_class(self):
        """test reload valid json with unknow class"""
        data = {
            'UnknownClass.54321': {
                '__class__': 'UnknownClass',
                'id': '54321'
            }
        }
        with open("file.json", "w") as f:
            json.dump(data, f)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


class TestFileStorageNoFile(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_file_path_when_no_file(self):
        """Test __file_path attribute when there's no file"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_when_no_file(self):
        """Test __objects attribute when there's no file"""
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all_when_no_file(self):
        """Test all() method when there's no file"""
        objects = self.storage.all()
        self.assertEqual(objects, {})

    def test_new_when_no_file(self):
        """Test new() method when there's no file"""
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, objects)

    def test_save_when_no_file(self):
        """Test save() method when there's no file"""
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
