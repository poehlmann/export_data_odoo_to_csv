#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ********************************************************#
# Importación Productos#
# ********************************************************#
import sys
import collections
import csv
import xmlrpclib

# HOST='192.168.20.87'
# PORT=80
# DB='roghurv01.redeskbolivia.com'
# USER='bruno.poehlmann@gmail.com'
# PASS='admin'
# url ='http://%s:%d/xmlrpc/' % (HOST,PORT)

HOST = 'localhost'
PORT = 8010
DB = 'femenina'
USER = 'admin'
PASS = 'Redesk2017'
url = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

common_proxy = xmlrpclib.ServerProxy(url + 'common')
object_proxy = xmlrpclib.ServerProxy(url + 'object')
uid = common_proxy.login(DB, USER, PASS)

def _create():

    args = [('id', '<>', 0)]  # consulta
    global product
    list_product=[]
    ids = object_proxy.execute(DB, uid, PASS, 'product.template', 'search', args)
    for id in ids:
        product = object_proxy.execute(DB, uid, PASS, 'product.template', 'read', id, ['id', 'name'])
        list_product.append(product[0])
    download_dir = "/home/bpm/Escritorio/thefile.csv"
    csv = open(download_dir, "w")
    columnTitleRow = "id, name\n"
    csv.write(columnTitleRow)
    for dic in list_product:
        # print dic
        for key in dic.keys():
            row = str(dic[key])+","
            csv.write(row)
        csv.write('\n')

def __main__():
    print 'Ha comenzado el proceso'
    _create()
    print 'Ha finalizado la carga tabla'

__main__()
