### 1) 다음 중 데이터 제어어(DCL)에 해당하는 명령어는?
1) INSERT
2) RENAME
3) COMMIT
4) REVOKE

- 답: 4
- 해설: 데이터 제어어는 데이터베이스에 접근하고 객체들을 사용할 수 있도록 권한을 부여하거나 회수하는 명령어로 GRANT, GEVOKE가 있다


### 2) 다음 중 아래 내용의 범주에 해당하는 SQL 명령어로 옳지 않은 것은?
- 테이블의 구조를 생성, 변경, 삭제하는 등 데이터 구조를 정의하는데 사용되는 명령어
1) CREATE
2) GRANT
3) ALTER
4) DROP

- 답: 2
- 해설: 데이터의 구조를 정의하는 명령어는 DDL(데이터 정의어)에 해당하며 DDL 문으로는 CREATE, ALTER, DROP, RENMAE 등이 있다


### 3) 아래 내용에 해당하는 SQL 명령어의 종류를 작성하시오
- 논리적인 작업의 단위를 묶어 DML에 의해 조작된 결과를 작업단위(Transaction)별로 제어하는 명령어인 Commit, Rollback, Savepoint 등이 여기에 해당하며, 일부에서는 DCL로 분류하기도 한다

- 답: TCL
- 해설: Transaction를 제어하는 명령어는 TCL이다

### 4) 데이터베이스를 정의하고 접근하기 위해서는 데이터베이스 관리 시스템과의 통신수단이 필요한데 이를 데이터 언어(Data Language)라고 하며, 그 기능과 사용 목적에 따라 DDL, DML, DCL로 구분된다. 다음 중 데이터 언어와 SQL 명령어에 대한 설명으로 가장 부적절한 것은?
1) 비절차적 데이터 조작어(DML)은 사용자가 무슨 데이터를 원하며, 어떻게 그것을 접근해야 되는지를 명세하는 언어이다
2) DML은 데이터베이스 사용자가 응용 프로그램이나 질의어를 통하여 저장된 데이터베이스를 실질적으로 접근하는데 사용되며 SELECT, INSERT, DELETE, UPDATE 등이 있따
3) DDL은 스키마, 도메인, 테이블, 뷰, 인덱스를 정의하거나 변경 또는 제거할 때 사용되며 CREATE, ALTER, DROP, RENAME 등이 있다
4) 호스트 프로그램 속에 삽입되어 사용되는 DML 명령어들을 데이터 부속어라고 한다

- 답: 1
- 해설 : As-Is: 비절차적 데이터 조작어(DML)는 사용자가 무슨 데이터를 원하는 지만을 명세함
- To-Be: 비절차적 데이터 조작어(DML)는 사용자가 무슨 데이터를 원하는 지만을 명세하지만, 절차적 데이터 조작어는 어떻게 데이터를 접근해야 하는지 명세한다. 절차적 데이터 조작어로는 PL/SQL(오라클), T-SQL(SQL server) 등이 있다

### 5번
  답: 1, 2
- 해설: DDL: CRATE, DROP, ALTER, RENAME
- DML: SELECT, INSERT, UPDATE, DELETE
- DCL: GRANT, REVOKE
- TCL: COMMIT, ROLLBACK

### 6번