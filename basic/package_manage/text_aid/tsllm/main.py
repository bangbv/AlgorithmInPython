import sys
# sys.path.append('/Users/bangbui/workspace/AlgorithmInPython/basic/package_manage/text_aid')

from test.my_test_package import train

if __name__ == '__main__':
    config = {
        'name': 'test'
    }
    print(f"Running with config: {config}")
    # train(config)