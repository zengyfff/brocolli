import pytest
import warnings


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    pytest.main(['-p', 'no:warnings', '-v', 'test/op_test/trt'])