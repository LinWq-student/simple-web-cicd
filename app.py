import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_contains_title(client):
    """测试首页包含学号和姓名"""
    rv = client.get('/')
    assert rv.status_code == 200
    data = rv.data.decode('utf-8')
    assert '学号' in data
    assert '姓名' in data

def test_health_check(client):
    """健康检查接口返回健康信息"""
    rv = client.get('/')
    assert rv.status_code == 200
