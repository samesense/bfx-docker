#!/usr/bin/env python2

import yaml
import argparse
import os
import subprocess
import time
import itertools
from functools import reduce

outputDirectory = '/bbx/mnt/output/'

def parseYAML():
    yaml_file = os.environ['YAML']
    if not os.path.exists(yaml_file):
        print 'YAML file {} does not exist'.format(yaml_file)
        exit(1)

    valid_status = subprocess.call(['validate-biobox-file', '--input', yaml_file, '--schema', '{}/share/schema.yaml'.format(os.environ['PREFIX'])])

    if valid_status != 0:
        print 'Imput YAML file is invalid. Check the RFC!'
        exit(2)

    yaml_d = yaml.load(open(yaml_file, 'rt'))
    yaml_d['arguments'] = reduce(lambda a, b: dict(a, **b),yaml_d['arguments'])

    cache_folder = yaml_d['arguments']['cache'][0]['value']
    taxonomy_folder = yaml_d['arguments']['database'][0]['value']

    cache_folder = cache_folder if len(cache_folder) else '/tmp'
    if not os.access(cache_folder, os.W_OK):
        print('Cache folder {} is not writeable'.format(cache_folder))
        exit(3)

    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)

    if not os.access(outputDirectory, os.W_OK):
        print('Output folder {} is not writeable'.format(cache_folder))
        exit(3)

    tasks = []
    for fq in yaml_d['arguments']['fastq']:
        if not os.path.exists(fq['value']):
            print 'Input FASTQ file does not exists.'
            exit(4)
        tasks.append(fq['value'])
    return tasks

def main():
    tasks = parseYAML()
    output_file = '{}/mp2_result__{}'.format(outputDirectory, os.path.basename(datetime.datetime.now().strftime ("%Y%m%d%H%M%S")))

    command = ( '{0}/src/{1}/metaphlan2.py '
                '--input_type fastq '
                '--nproc `nproc` '
                '--bowtie2out {2}/out.bowtie2 '
                '{3} {4}.orig'.format(os.environ['PREFIX'],os.environ['TOOLNAME'], outputDirectory, ','.join(tasks), output_file))
        
        print "EXECUTING TASK"
        start = time.time()
        mp2ec = os.system(command)
        end = time.time()
        print "TASK COMPLETED IN {} SECONDS. MetaPhlAn2 output is located in {}".format(end-start, output_file)
if __name__ == '__main__':
    main()
