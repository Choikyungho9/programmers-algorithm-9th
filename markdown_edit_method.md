# MarkDown
## MarkDown Syntax

**Markdown**이란 마크업 언어의 일종으로 읽기도, 쓰기도 쉬운 언어를 지향합니다. 확장자는 .md입니다.
주로 github의 readme.md 파일에 자주 사용되며
현재 스팀(Steem)의 디앱(dapp) 스팀잇(Steemit)의 문법으로 사용 되고 있지요.

## No.1 -  글자 크기 조절

```
- #의 개수로 글자크기를 조절합니다. (#~######) 
# 안녕 = <h1>안녕
## 안녕 = <h2>안녕
### 안녕 = <h3>안녕
#### 안녕 = <h4>안녕
##### 안녕 = <h5>안녕
###### 안녕 = <h6>안녕  
#을 써도 되고, h1~h6을 써도 됩니다.
```

# 안녕
## 안녕 
### 안녕 
#### 안녕 
##### 안녕 
###### 안녕

## No 2. 강조

```
- 굵게 --->  **굵게**  
- 기울이기 ---> *기울임* 
- 굵으면서 기울이기 --> ***굵으면서 기울이기***
- 취소선 만들기 ---> ~~취소선~~ 
- 밑줄 긋기 ---> <u>밑줄</u> 
```

**굵게**


*기울임*


***굵으면서 기울이기***


~~취소선~~


<u>밑줄</u>




## No.3 -  인용
```
> 첫 번째 단계 인용

>> 두 번째 단계인용
```
</br>
> 첫 번째 단계 인용

>> 두 번째 단계인용

## No.4 - 수평선
```
1) *** (일반 수평선)

2) --- (일반 수평선)
```
</br>
***
---
(위의 수평선 2개를 ***와 --- 로 만들었습니다.)

## No.5 클릭 (하이퍼링크)
```

Click [google](https://google.com)

구글 하이퍼링크
```

Click [google](https://google.com).  
https://google.com
링크를 깔끔하게 숨기고 싶을 때, 쓰면 되겠습니다.
## No.6 이미지 업로드하기
```
![image description](이미지링크)
```

![image description](https://cdn.steemitimages.com/DQmbL5n9pjYNrgZdGsF8he6FhoKaMX71vaGzcXTuSxoRm7W/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-02%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.55.03.png)




## No.7 테이블 
```
Header 1| Header 2
------------ | -------------
Cell 1 | Cell 2
Cell 1 | Cell 2
```
Header 1 | Header 2
------------ | -------------
Cell 1 | Cell 2
Cell 1 | Cell 2

## No.8 인라인 형태 (코드블럭)

![스크린샷 2021-06-02 오후 10.20.40.png](https://cdn.steemitimages.com/DQmTYtnQkYukst8ZiqzSy35d4kTKwm3ecr3gMijcwNPVRX9/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-02%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.20.40.png)


`<코드블럭>`(해당 글자 부분만 인라인 형태로 만듬.)
또는
```
코드블럭 (해당 글의 전체 줄을 다 인라인 형태로 만듬.)
```


## 9. 코드블럭 만들기

```

console.log('your message')

```

위에 

```ts 혹은 js 혹은 java 혹은 Kotlin 등 

console.log('your message')

```



## 10. 줄바꿈

마크다운에서 Enter 하나로 줄바꿈이 되지 않습니다 줄을 바꾸기 위해 `</br>`을 쓸수도 있으나
라인의 마지막에 공백 두칸 space 두번 하면 줄바꿈이 가능합니다.
문단을 구분하려면 Enter를 두번 누릅니다. 

## 11. Highlighting<br>
-> ₩₩₩(맥북의 경우 tap누르고)하면 코드블럭이 생기는데, ₩₩₩python ₩₩₩javascript이런식으로 하면 highlighting된다.
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

## 12. TaskLists
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

## 13. Emoji
```
@octocat :+1: This PR looks great - it's ready to merge! :shipit:
```
@octocat :+1: This PR looks great - it's ready to merge! :shipit:

For a full list of available emoji and codes, check out the [Emoji-Cheat-Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md).



## 14. Ignoring Markdown formatting
You can tell GitHub to ignore (or escape) Markdown formatting by using \ before the Markdown character.

Let's rename \*our-new-project\* to \*our-old-project\*.

Rendered escaped character

For more information, see Daring Fireball's "Markdown Syntax."
