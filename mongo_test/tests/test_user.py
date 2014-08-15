#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os

from pymongo import MongoClient
from mongo_test.fixtures import setup_data, oid_con, teardown_data

conn = MongoClient(port=27017)
db = conn.myapp

from mongo_test.handlers import startup_handle
startup_handle()


class TestUser(unittest.TestCase):

    def setUp(self):
        current_path = os.path.abspath(os.path.dirname(__name__))
        self.fixture_path = os.path.join(current_path, 'fixtures/user_fixture.yml')
        setup_data([self.fixture_path], db)

    def test_find_user(self):
        # Fetch user by id
        user = db.users.find_one(query={'_id': oid_con(1)})
        # Check pymongo works as advertised.
        assert user['_id'] == oid_con(1)
        assert user['username'] == 'idbentley'

    def tearDown(self):
        teardown_data([self.fixture_path], db)
