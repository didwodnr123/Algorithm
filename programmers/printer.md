## [프로그래머스] 프린터 - 파이썬

[source: programmers](https://programmers.co.kr/learn/courses/30/lessons/42587)

#### 문제 설명

일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

```
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
```

예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

#### 제한사항

- 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
- 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
- location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.

#### 입출력 예

| priorities         | location | return |
| ------------------ | -------- | ------ |
| [2, 1, 3, 2]       | 2        | 1      |
| [1, 1, 9, 1, 1, 1] | 0        | 5      |

##### 입출력 예 설명

예제 #1

문제에 나온 예와 같습니다.

예제 #2

6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다.



### 풀이

```python
from collections import deque 

def solution(priorities, location):
    answer = 0
    # enumerate를 사용해서 index와 value값을 튜플로 묶어서 매핑시켜 준다.
    queue = deque([(v,i) for i,v in enumerate(priorities)])
    while queue:
        item = queue.popleft()
        # 큐에서 item보다 큰 값이 하나라도 존재하면 큐 맨 뒤로 보낸다.
        if queue and max(queue)[0] > item[0]:
            queue.append(item)
        # 큰 값이 하나도 없다면 큐에 다시 집어넣지 않는다.
        else:
            answer += 1
            # location 즉 원하는 Index 값과 큐에서 나가는 값의 Index가 같으면 반복문 즉시 종료. 
            if item[1] == location:
                break
    
    return answer
```

- **`deque` 을 사용하는 이유**: `list`를 사용하는 것보다 빠르다.
- `index`와 `value`값을 하나의 튜플로 묶어줘서 사용해야 **unique** 한 특징을 유지할 수 있다. (eg. 1, 1, 1, 1은 구별 불가)
- **`index`와 `value`값을 뒤집어서 저장하는 이유**: `max(queue)`를 했을 때 앞에 있는 값을 기준으로 max값 추출하기 때문이다.
- **첫 조건문에서 `if` `queue` 조건을 추가해야하는 이유**: 마지막 하나를 popleft() 했을 때, queue가 비어있기 때문에 max(queue)[0]에서 오류가 발생한다. 