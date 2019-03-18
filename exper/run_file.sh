#!/bin/sh

#python depoly_script.py "/data1/bzhang/SEG/PSPNet-master/exper/config/depoly.prototxt" "/data1/bzhang/SEG/PSPNet-master/exper/config/parsing.caffemodel" "/data1/bzhang/dataset/oppo_dataset/test_instance/"

mkdir result

project_path=$(cd `dirname $0`; pwd)
cd $project_path

echo $project_path
echo $1

python deploy_script.py $project_path/$1/deploy.prototxt $project_path/$1/parsing.caffemodel $2
