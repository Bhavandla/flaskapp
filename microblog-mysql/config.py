WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

import os
MYSQL_DATABASE_USER= "root"
MYSQL_DATABASE_PASSWORD= "bhava"
MYSQL_DATABASE_DB= "EmpData"
MYSQL_DATABASE_HOST= "localhost"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + MYSQL_DATABASE_USER + ':' + MYSQL_DATABASE_PASSWORD + '@' + MYSQL_DATABASE_HOST + "/" + MYSQL_DATABASE_DB
SQLALCHEMY_MIGRATE_REPO = os.path.join(SQLALCHEMY_DATABASE_URI, 'db_repository')