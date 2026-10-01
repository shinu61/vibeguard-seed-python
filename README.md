# vibeguard-seed-python

VibeGuard 파이프라인 확인용 시드 리포 — **패치해도 안 깨지는 경우**.

- `requirements.txt`에 취약한 버전을 일부러 고정했다: `urllib3==1.24.1`(높음·보통), `joblib==1.1.0`(치명적)
- 테스트 6개는 패치 전에도 전부 통과하고, 안전 버전으로 올린 뒤에도 통과한다
- lock 파일은 두지 않는다(완전 지원 대상 형태)
