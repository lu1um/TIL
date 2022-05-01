# JavaScript로 로또만들기

### 코드

```javascript
const resultSection = document.querySelector('section#result')
const lottoButton = document.querySelector('button#lottoButton')
const ballList = document.createElement('ul')
const balls = []
for (let i=0;i<6;i++) {
    const ball = document.createElement('li')
    ball.setAttribute('class', 'ball')
    balls.push(ball)
}
ballList.setAttribute('class', 'ball-list')

lottoButton.addEventListener('click', event => {
    const lotto = []
    let tmp
    for (let i=0;i<6;i++) {
        while (lotto.includes(tmp = _.random(1, 45))) {}
        // _.sampleSize(iterable, n)
        lotto.push(tmp)
        balls[i].innerText = tmp
        let color
        let textColor = ''
        if (tmp > 40) color = 'green'
        else if (tmp > 30) {
            color = 'black'
            textColor = ' color: white;'
        }
        else if (tmp > 20) color = 'red'
        else if (tmp > 10) color = 'skyblue'
        else color = 'gold'

        balls[i].setAttribute('style', `background-color: ${color};${textColor}`)
    }
    balls.sort((a, b) => {
        return a.innerText - b.innerText
    })  // sort 쓰는법 : a - b가 0보다 크면 정순, 작으면 역순으로 정렬해준다.
    ballList.append(...balls)
    resultSection.appendChild(ballList)
})
```

- 배울점이 머엿지
