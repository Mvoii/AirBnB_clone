#!/usr/bin/python3
"""
Test suite for base_model dict
"""
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime
import os
from time import sleep

class TestBaseModelDict(unittest.TestCase):
    """
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
    """
    def test_base_model_dict(self):
        """
        Test the base model dictionary
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["name"], "My_First_Model")
        self.assertEqual(my_model_json["my_number"], 89)

        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)

    def test_base_model_save(self):
        """
        Test the base model save method
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(type(my_model.created_at) is datetime)
        self.assertTrue(type(my_model.updated_at) is datetime)
        

    def test_base_model_reload(self):
        """
        Test the base model reload method
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertTrue(type(my_new_model.created_at) is datetime)
        self.assertTrue(type(my_new_model.updated_at) is datetime)
        

    def test_base_model_save_reload(self):
        """
        Test the base model save and reload method
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertTrue(type(my_new_model.created_at) is datetime)
        self.assertTrue(type(my_new_model.updated_at) is datetime)
        
        self.assertTrue(my_model.id == my_new_model.id)
        self.assertTrue(my_model.name == my_new_model.name)
        

