#!usr/bin/python3
"""
    Test module for BaseModel class.
"""
from models.base_model import BaseModel
import unittest
import datetime


class TestBaseModel(unittest.TestCase):
    """
        test class for base_model class.
    """

    def test_empty(self):
        """
            test class instantiation with no arguments.
        """
        m1 = BaseModel()

    def test_id_unique(self):
        """
            tests if an id is unique.
        """
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertNotEqual(m1.id, m2.id)

    def test_id_type(self):
        """
            tests if generated id is of type string.
        """
        m1 = BaseModel()
        self.assertEqual(type(m1.id), str)

    def test_change_id(self):
        """
            tests when id is changed manually.
        """
        m1 = BaseModel()
        m2 = BaseModel()
        m1.id = m2.id
        self.assertEqual(m1.id, m2.id)

    def test_type_created_at(self):
        """
            tests the type of attribute created_at.
        """
        m1 = BaseModel()
        self.assertEqual(type(m1.created_at), datetime)

    def test_type_updated_at(self):
        """
            tests the type of attribute updated_at.
        """
        m1 = BaseModel()
        self.assertEqual(type(m1.updated_at), datetime)

    def test_created_updated_compared(self):
        """
            tests that created at is not greater than updated at
            when instantiated and when updated.
        """
        m1 = BaseModel()
        self.assertEqual(m1.updated_at, m1.created_at)
        m1.save()
        date1 = m1.created_at
        date2 = m1.updated_at
        self.assertLess(date1, date2)

    def test_createdat_two_objects(self):
        """
            tests that created_at is greater for a second created
            object than the first.
        """
        m1 = BaseModel()
        m2 = BaseModel()
        date1 = m1.created_at
        date2 = m2.created_at
        self.assertLess(date1, date2)

    def test_str_return(self):
        """
            tests the str return of class BaseModel.
        """
        m1 = BaseModel()
        class_name = "BaseModel"
        m1_id = str(m1.id)
        m1_dict = str(sorted(m1.__dict__))
        str_m1 = "[{}] ({}) {}".format(class_name, m1_id, m1_dict)
        self.assertEqual(str_m1, str(m1))

    def test_str_return_new_id(self):
        """
            tests that str will update with an updated id.
        """
        m1 = BaseModel()
        class_name = "BaseModel"
        m1.id = "1"
        m1_dict = str(sorted(m1.__dict__))
        str_m1 = "[{}] (1) {}".format(class_name, m1_dict)
        self.assertEqual(str_m1, str(m1))

    def test_save(self):
        """
            tests the save method and if the updated_at is
            greater than the created_at attribute after update.
        """
        m1 = BaseModel()
        date1 = m1.created_at
        m1.save()
        date2 = m1.updated_at
        self.assertGreater(date2, date1)

    def test_to_dict(self):
        """
            tests the method to_dict and if it matches self.__dict__.
        """
        m1 = BaseModel()
        self.assertDictContainsSubset(m1.__dict__, m1.to_dict)
        class_dict = {"__class__": "BaseModel"}
        self.assertDictContainsSubset(class_dict, m1.to_dict)

    def test_to_dict_createdupdated(self):
        """
            tests if to_dict contains str iso of created_at
            and updated_at public attributes.
        """
        m1 = BaseModel()
        date1 = m1.updated_at.isoformat()
        date2 = m1.created_at.isoformat()
        class_dict = {"updated_at": date1, "created_at": date2}
        self.assertDictContainsSubset(class_dict, m1.to_dict)
"""
    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """

    def test_  (self):
        """

        """
"""
