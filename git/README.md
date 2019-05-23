# Git

## git 사용법

### Branch 만들기

  1. 본인의 `branch`확인하기 위해서는 `conda`의 경우 `branch`가 나오는 것을 확인 했는데
  `cmd`의 경우에는 `branch`가 나오지 않습니다. 이때 `git branch`를 사용하면 본인이 지금
  사용하고 있는 `branch`이름이 나오게 되고 또한 지금 만들어져 있는 `branch`까지 있습니다.
  본인이 사용하고 있는 `branch`는 쉽게 표시되어 나오니 따로 걱정 할 필요는 없습니다.

  2. 이제 branch를 새로 만들고 이동을 하게 될텐데 `branch`를 새로 만드는 코드는
  `git branch branch이름` 예를 들면 `git branch model` 이런식으로 만들면 됩니다.
  만약 새로 만들게 된다면 본인의 `branch`가 `dev`에 있는지 확인하고 만들어 주세요. 만약
  본인의 `branch`가 `dev`가 아니라면 `git checkout dev`로 `branch` 이동 후 새로
  만들어 주시길 바랍니다.

  3. 만약 `branch`에서 모든 활동을 마무리하고 지워야 한다면 `git branch -d branch명`
  을 사용하여 삭제하면 됩니다. 삭제하기 전에 내가 `push`를 해야하는 파일이나 폴더가 있는지
  다시한번 확인하고 사용하시면 됩니다.


### Repository에 push하기
  1. `git status`를 치게되면 아직 `add`가 안된 파일이나 폴더는 빨간색으로 나오게 됩니다.
  여기에서 내가 `git repository`로 올리고 싶은 파일이 있으면 `git add 경로`의 방식으로
  쓰면 됩니다.

  2. `add`가 된 파일이나 폴더는 `git status`를 다시 입력하면 녹색으로 변경되어 있는것을
  확인할 수 있습니다. 만약에 내가 변경한 파일이나 폴더를 한꺼번에 올리고 싶다 라고 하면
  `git add all`이라는 명령어를 사용하면 되는데 이 방법은 잘못하면 올리고 싶지 않은
  파일이나 폴더까지 올라갈 수 있기 때문에 권장하지는 않습니다.

  3. 이제 `add`가 되었다며 `commit`을 해야 하는데 이때는 `git commit -m '코드에 대한
  간략한설명'` 이런 방식으로 사용 하면 됩니다. 코드에대한 간단한 설명의 예를 들어보면
  'DB에 대한 모델 생성'과 같은 방식으로 간단하게 남기면 됩니다.

  4. `commit`까지 남겼다면 이제 `push`를 해야하는데 이때 주의 할 점은 절대 `master`로
  `push`하면 안됩니다. 본인이 사용하고 있는 `branch`에서 `push`를 한 다음 `dev`의
  `branch`에다가 `merge`를 한 다음 이상이 없게 되면 관리자인 제가 `master`에다가 `push`
  를 할겁니다. 그러니 본인의 `branch`에다가만 `push`를 하면 됩니다. 명령어는
  `git push origin branch명`으로 하면 됩니다.

### git merge

  1. 이제 `branch`를 `dev`에서 본인이 만든 `branch`로 이동 한 후 코드를 만들었을 겁니다.
  그러면 이제 `dev`로 돌아와서 본인이 쓴 폴더나 파일을 합쳐야 하는데, 이 때 사용하는 코드가
  `merge`입니다. 이제 본인이 활동하던 `branch`에서 끝내고 `push`를 했다면 `dev`로 다시
  돌아와서 일단은 `git fetch origin/dev` 로 변경된게 있는지 확인합니다. 여기서 주의할 점은
  `branch`위치는 `dev`여야 합니다. 그 다음에 만약 변경된 점이 있다고 하면
  `git merge origin/dev`로 `merge`를 한 후 된걸 확인합니다.

  2. 이제 `dev`의 `branch`에서 자신이 활동한 `branch`를 `merge`해야 하는데
  `git merge origin/본인의 branch명` 방식으로 하면 됩니다. `merge`가 다 된다면 이제
  `dev`로 `push`하면 됩니다.