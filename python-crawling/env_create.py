# base64 모듈
import base64, json;

env = {}
env['account'] = "test@naver.com"
env['pwd'] = "test"
env['name'] = "홍길동"
env['to'] = "receive@naver.com"
# {"account":"test@naver.com", "pwd":"test", "name":"홍길동", "to":"receive@naver.com"}

envs = base64.b64encode(json.dumps(env).encode('ascii')).decode('ascii')
# 여기서 나온 값을 환경변수에 셋팅합니다.
print('ENV naver_account=', envs)

env = json.loads(base64.b64decode(envs).decode('ascii'))
print(env)