================
MongoDB Test Util
================

This library provides a handful of useful functionality for easing the testing
of systems that rely on MongoDB as a datastore

-------------------------
Start and Teardown mongod
-------------------------

For most use cases, you can use this snippet to startup a mongod instance
for your test environment:::

    from mongo_test.handlers import startup_handle
    startup_handle()

To tear an instance down if one exists:::

    from mongo_test.handlers import teardown_handle
    teardown_handle()

--------
Fixtures
--------

MongoTest allows you to specify fixtures in yaml, with a few conveniences

i.e.::

    from mongo_test.fixtures import setup_data
    import_data([path, ...])

A sample yaml file would look something like:::

    `user_fixture.yml`
        configuration:
            collection: users
            drop: true
        simple_user:
            _id: !oid 1
            username: idbentley
            first_name: Ian
            last_name: Bentley

`!oid` is a custom constructor provided by MongoTest to allow you to test
object ids as having any integer seed you specify.  You can access the
constructor directly with:::

    from mongo_test.fixtures import oid_con
    id = oid_con(1)

------------------
A complete example
------------------

See the tests for a complete simple example.

