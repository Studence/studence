@echo off
set module=Module
mkdir %1%module%
cd %1%module%
set init=__init__
type nul > %init%.py
set comparetor=Comparetor
type nul > %1%comparetor%.py
set convertor=Convertor
type nul > %1%convertor%.py
set helper=Helper
type nul > %1%helper%.py
set config=Config
type nul > %1%config%.py
set search=Searcher
type nul > %1%search%.py
set service=Service
type nul > %1%service%.py
set tablename=TableName
type nul > %1%tablename%.py
set updator=Updator
type nul > %1%updator%.py
set cache=Cache
type nul > %1%cache%.py
set PbIndexGenerator=PbIndexGenerator
type nul > %1%PbIndexGenerator%.py
set UpdateListner=UpdateListner
type nul > %1%UpdateListner%.py
cd ..



