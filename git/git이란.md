# 1. Git
- 분산 버전 관리 시스템으로 코드의 버전을 관리하는 도구
- 2005년 리눅스 커널을 위한 도구로 리누스 토르발스 개발
- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업 조율
- 로컬에서 자신의 개발 소스에 대한 섬세한 관리 가능
- Remote Repository(원격 저장소)에 영구적인 백업 및 다양한 협업 가능

# 2. Git 장점
- **오프라인 작업 가능** : git은 저장소를 로컬에 복제하고, 로컬 저장소에 있는 히스토리도 그대로 유지된다. 이는 서버에서 새로운 자료를 받아올 수 없을뿐 이외에는 오프라인 상태에서 대부분의 형상관리 기능을 이용할 수 있다 => 일종의 로컬 서버로 작용됨
- **속도 빠름** : 각각의 개발자들이 모두 분산처리 서버의 master이 되기때문에 서버가 직접해야 될 일들이 많이 줄어듬
- **일시적인 서버 장애가 있어도 개발을 계속할 수 있다** : 로컬 저장소 이용하면 됨
- **Branch(가지치기)가 비교적 쉬움**
- **Merge(병합) 문제가 덜 발생함** : 서버의 자료를 가져와 로컬에서 병합하고 이를 다시 올리는 형태이기 때문
- **Staging 지원** : Commit(커밋)하기 전 사용해야하는 스테이징 단계를 지원함
- **Tool 많음** : 수많은 개발자용 툴이 Git을 자체 지원하거나, Git용 플러글인이 있음, 초보자를 위한 GUI부터 전문자용 Diff툴까지 Git사용에 도움이 되는 툴이 많음

# 2. Git 단점
- **기존 형상관리 도구에 비해 덜 직관적, 배우기 힘듬** : 처음배우는 경우 어디까지가 서버에 영향을 미치는 행위이고 어디까지가 로컬에서 안전하게 할 수 있는 일인지 명확하게 이해하기 어려워 명령어 하나하나에 두려움을 느낄 수 있음
- **한 번에 여러 브랜치나 여러 태그에 걸쳐서 커밋을 할 수 없다** : 내가 만든 사소한 변동사항이 다른 브랜치에 자동적으로 알려지지 않고 나중에 취합하는 시점이 돼서야 반영됨, 타 브랜치와 병합시 충돌의 원인이 될 수 있음
- **커밋 히스토리가 영원히 안전하게 저장된다고 보장할 수 없음** : 중앙 집중형 형상관리에서 체크인을 하고 나면 서버에 문제가 생기지 않는 한 항상 안전하고 언제든 과거 기록을 볼 수 있으나, git에서는 Push를 한 내용이라도 해당 브랜치가 다른 브랜치에 병합되기 전에 삭제되어버리면 나중에 해당 내용에 접근할 수 없음

# 3. Git 저장소
- (Github)[]
- GitLab
- Bitbucket
- Azure DevOps

# 4. 자체 호스팅
 - 외부에서 제공되는 서비스 형태가 아닌, 설치형 Git 서버는 리눅스 서버라면 별다른 추가 프로그램 없이 리눅스의 기본 프로그램(SSH 등)과 배포본에 들어있는 패키지 만으로 서버 구동 가능

 # 5. CLI/GUL 사용
 - Git 사용시 CLI/GUL 둘 다 사용 가능함
 - GUI 프로그램의 대부분은 Git 기능 중 일부만 구현하기 때문에 단순
 - CLI를 사용할 경우 GUI도 사용 가능하지만 반대는 성립하지 않음
 - Visual Studio 사용 시 git 프로젝트를 사용하면 자동으로 내장된 자체 git GUI가 나타남

 # 6. Git 사용법
 - [Git 간편 안내서](http://rogerdudler.github.io/git-guide/index.ko.html)
- [누구나 쉽게 이해할 수 있는 Git 입문](https://backlog.com/git-tutorial/kr/intro/intro1_1.html)
- [**생활코딩**](https://opentutorials.org/course/1) : [Git](https://www.youtube.com/playlist?list=PLuHgQVnccGMCNJESahrVV-uYGMNYK_vMf), [Git CLI](https://www.youtube.com/playlist?list=PLuHgQVnccGMATJK16UJ9Fjay0ozrSZKiI), [Git CLI-브랜치 & 충돌](https://www.youtube.com/playlist?list=PLuHgQVnccGMDU5eAzOz2dZ9KXJF6dkNg3), [Git CLI - 백업](https://www.youtube.com/playlist?list=PLuHgQVnccGMBJr3eVXGvYHDvGNcogEy7v), [Git CLI - 협업](https://www.youtube.com/playlist?list=PLuHgQVnccGMA4LgLoH07e7uEbRbi92Dd2), [Git CLI - Cherrypick & Rebase](https://www.youtube.com/playlist?list=PLuHgQVnccGMAb_nOiego7BqfKTRcXsUrB), [GitHub Pull Request](https://www.youtube.com/playlist?list=PLuHgQVnccGMBXv1OKe3Hn3Jq6F735-uWm), [VSCode로 다루는 Git](https://www.youtube.com/playlist?list=PLuHgQVnccGMAQvSVKdXFiOo51HUD8iQQm)
- [progit](http://dogfeet.github.io/articles/2012/progit.html) : GitHub의 CIO인 schacon이 쓴 progit
- [브랜치 배우고 체험해보기](https://learngitbranching.js.org/?locale=ko)

# 7. 브랜치(branch) 주의사항
- 현실 프로젝트 시 보통 브랜치를 분리하라고 하지만 나중에 병합(merge) 단계에서 더 큰 충돌이 발생하는 경우가 많아 함부로 브랜치 기능을 사용하는 것에 주의해야 함
- 매우 거대한 기능을 개발하거나 앞으로 합칠 생각이 없는, 즉 다른 가지로 뻗어나가는 버전을 따로 사용하고 싶을 때 브랜치 사용

# 8. 기타
- Git은 파일이나 커밋 등 모든 오브젝트를 SHA-1로 해시한 식별자를 통해 관리
- 이에 개발자 `리누스 토르발스`는 한다며 동의하지 않음
> Git은 데이터를 해시하기만 하는 것이 아니라, 거기에 타입과 길이 필드를 측량함