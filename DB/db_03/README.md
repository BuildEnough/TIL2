###  1. 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql
SELECT smoking, count(*) FROM healthcare WHERE smoking != '' GROUP BY smoking;
```
 
###  2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql
SELECT is_drinking, count(*) FROM healthcare WHERE is_drinking != '' GROUP BY is_drinking;
```
 
### 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.

```sql
SELECT is_drinking , count(*) FROM healthcare WHERE blood_pressure != '' AND blood_pressure >= 200 GROUP BY is_drinking;
```

### 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.

```sql
SELECT count(sido) >= 50000, sido 시도코드, count(sido) 사람의_수 FROM healthcare GROUP BY sido;
```

### 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.

> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.

```sql
SELECT height, count(id) 사람의_수 FROM healthcare GROUP BY height ORDER BY height DESC LIMIT 5;
```

### 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.

```sql
```

### 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.

```sql 
SELECT is_drinking,  AVG(waist) 평균_허리둘레, count(*) 사람의_수 FROM healthcare WHERE is_drinking != '' GROUP BY is_drinking;
``` 

### 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.

> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

```sql
```

### 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.

> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

```sql
SELECT age, AVG(height) '평균 키', AVG(weight) '평균 몸무게' FROM healthcare GROUP BY age HAVING AVG(height) >= 160 and AVG(weight) >= 60;
```

### 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.

```sql
SELECT is_drinking '음주', smoking '흡연', ROUND(AVG(weight/((height*0.01)*(height*0.01))), 2) BMI FROM healthcare GROUP BY 음주, 흡연 HAVING NOT 음주="" AND NOT 흡연="";
```