#!/bin/sh

flask db upgrade

python $@
