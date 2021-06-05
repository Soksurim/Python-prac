# SQLD - 데이터 모델링

**1. 모델링의 3대 특징** 
- 추상화
- 단순화
- 명확화

- 모델링은 현실 세계의 복잡하고 구체적인 것을 단순 명확하게 추상화한다. 
- *구체화(x)*

#

**2. 데이터 모델의 추상화 수준** 

`개념 > 논리 > 물리`

- **개념 데이터 모델** : 추상화 수준이 높고 주로 핵심 엔터티와 그들간의 관계를 나타낸 데이터 모델. 업무중심적, 포괄적.
- **논리 데이터 모델** : 모든 엔터티, 속성. 관계를 도출하고 중복 제거를 위해 정규화를 적용. 업무에 대한 키, 속성, 관계 등을 정확하게 표현.
- **물리 데이터 모델** : 데이터베이스 이식을 위해 성능, 저장 등 물리 요소를 고려하여 설계.

#

**3. 인스턴스**
- 엔터티는 `인스턴스`의 집합이라고 할 수 있다. 예를 들어 부서는 인사, 총무, 영업 등이 존재할 수 있는데 인사, 총무, 영업 각각은 부서 엔터티의 인스턴스들이라고 할 수 있다.
    - 각 인스턴스의 성격을 구체적으로 설명하는 항목이 `속성`이고, `식별자`는 인터티의 여러 속성 중 각 인스턴스를 유일하게 식별할 수 있는 하나 이상의 속성을 의미.

#

**4. 엔터티**
- 변별할 수 있는 사물
- 데이터베이스 내에서 변별 가능한 객체
- 정보를 저장할 수 있는 어떤 것.
    
#

**5. 관계 (Relationship)**  

<img src="https://user-images.githubusercontent.com/66513003/118942125-66bb2480-b98d-11eb-8662-60f820695850.png" width="300">

- 계좌를 개설한 고객이 반드시 존재해야 한다.
- 고객과 계좌의 관계에서 고객의 식별자인 고객 번호가 계좌의 일반 속성으로 사용되므로 비식별자 관계이다. 계좌의 주민등록번호는 관계에 의해 생성된 관계속성이 아니며, 중복 속성 으로 볼 수 있다.
- 자식엔터티의 계좌 기준으로 부모인 고객 엔터티를 `필수 관계`로 정의했으므로 고객으로 등록한 고객만 계좌를 개설할 수 있다. 부모 엔터티인 고객 기준으로 자식인 계좌 엔터티를 `선택 관계`로 정의 (고객 쪽 관계선이 점선)했으므로 모든 고객이 계좌를 개설해야 하는 것은 아니다.

#

- 부모 엔터티의 식별자를 자식 엔터티의 식별자로 상속하면 '식별관계', 일반속성으로 상속하변 '비식별관계'라고 한다.
- 부모 엔터티의 식별자가 아닌 일반 속성을 자식 엔터티의 속성으로 정의한다면, 정상적인 관계속성이 아니다. 정혀 관련없이 이름만 같은 (=이름은 같지만 엔터티별로 의미가 다른) 속성이거나 부모 속성을 반정규화한 중복 속성일 수도 있다.

#

**6. 다른 엔터티와의 관계에 의해 생성된 속성**  

<img src="https://user-images.githubusercontent.com/66513003/118944847-e5b15c80-b98f-11eb-902d-f81c47d9651e.png" width="150">

- 관계 속성(외래 식별자)에는 FK(Foreign Key)표현을 추가한다.

#

**7. 데이터 모델**

<img src="https://user-images.githubusercontent.com/66513003/118945798-c0711e00-b990-11eb-9bef-62e3a180c0f6.png" width="400">

- 부서와 사원은 M:M관계이다.
- 사원은 반드시 하나 이상의 부서에 속해야 한다.
- 부서에는 동일 사원이 중복하여 소속될 수 없다.
- 부서소속사원은 부서와 사원 간 M:M 관계를 엔터티로 풀어서 재정의한 관계엔터티.
- 부서 기준으로 부서소속사원을 `1:M 선택 관계`로 정의했다. 따라서 부서가 여러 소속사원을 가질 수 있지만, 소속사원이 없는 부서도 존재할 수 있다. 
- 사원 기준으로 부서 소속사원을 `1:M 필수 관계로` 정의했으므로 사원을 여러 부서에 속할 수 있으며, 반드시 하나 이상의 부서에 속해야 한다.
- 부서소속사원의 식별자는 양쪽 부모로부터 상속한 부서번호와 사번이다. 두 값을 조합했을 때, 중복 인스턴스를 허용하지 않는다는 뜻이다. 따라서 한 부서에 소속사원이 여럿일 수 있지만, 같은 사원을 여러 번 등록할 수는 없다.

#

<img src="https://user-images.githubusercontent.com/66513003/118946989-ddf2b780-b991-11eb-976d-30b8e07f078f.png" width="400">

- **선택 관계** : 부모 인스턴스만 등록하고 자식 인스턴스는 등록하지 않아도 된다.

- **필수 관계** : 부모 인스턴스별로 자식 인스턴스를 반드시 등록해야 한다.

#### 참조 - **관계** https://doorbw.tistory.com/228

#

**8. 식별자**

<img src="https://user-images.githubusercontent.com/66513003/118949680-725e1980-b994-11eb-85b7-12c34b69c27e.png" width="400">

- 고객은 한번 이상 주문을 할 수 있다.
- 한 주문에 여러 상품을 구매할 수 있다.
- 고객은 동일 상품을 여러 번 주문할 수 있다.

- 주문상세의 식별자는 양쪽 부모로부터 `상속`한 주문번호와 상품번호다. 두 값을 조합했을 때 중복 인스턴스를 허용하지 않는다는 뜻이다. 따라서 한 주문(=같은 주문번호)에서 여러 상품을 주문할 수는 있지만, 같은 상품을 여러 번 주문할 수는 없다.

#
<img src="https://user-images.githubusercontent.com/66513003/118951939-7854fa00-b996-11eb-89e1-07df18d79ba3.png" width="400">

- 위 데이터 모델에서는 상품번호가 식별자가 아니므로 한 주문에서 같은 상품을 여러 번 주문할 수 있고, 그때마다 주문순번 값이 달라진다. 고객은 주문을 여러 번 할 수 있고, 한 주문에서 여러 상품을 주문할 수 있으므로 동일 상품을 여러 번 주문할 수 있다.

#
**9. 주문상세 엔터티의 주식별자에 대한 설명**

<img src="https://user-images.githubusercontent.com/66513003/118952239-bce09580-b996-11eb-9c9f-15c4f80f48c4.png" width="400">

- 주문상세 엔터티의 모든 인스턴스를 유일하게 식별할 수 있다.
- 주식별자 중 주문번호는 주문 엔터티로부터 상속받을 외래 식별자다.
- 주문순번 속성을 NULL값을 입력할 수 없다.

- 주식별자 중 주문순번은 중복값이 없어야 하지만 주문번호마다 꼭 `순차적으로 부여할 의무는 없다.`

#

**10. 부모 엔터티와 자식 엔터티가 식별관계를 가지는 데이터 모델**

<img src="https://user-images.githubusercontent.com/66513003/118955464-ae47ad80-b999-11eb-9293-f6b7bccf725e.png" width="400">

- 1, 2는 IE 표기법을 사용한 데이터 모델이다. 두 모델은 관계선이 둘 다 `점선`이므로 비식별관계를 표현하고 있다.
- 3, 4는 Barker 표기법을 사용했으며, 3번은 자식쪽 관계선에 `UID Bar(수직 실선)`를 표시했으므로 식별관계이다.

- 식별관계
    - 부모 엔터티의 식별자를 자식 엔터티의 식별자로 상속하는 관계
    - IE 표기법 : 관계선 전체를 실선으로 표현
    - Barker 표기법 : 자식 쪽 관계선에 UID Bar(수직 실선) 표시

#


**# 다음 데이터 모델이 틀린 이유**


<img src="https://user-images.githubusercontent.com/66513003/119096311-659dfc00-ba4e-11eb-81a3-47407794099c.png" width="400">

1. M쪽 엔터티의 주식별자를 1쪽 엔터티의 관계속성으로 정의했으므로 올바르지 않다.
2. 관계선을 반대로 그렸다. 관계선을 역으로 그린 후에 엔터티2의 속성1을 일반속성으로 정의(#를 *로 변경)하거나 식별자 관계(속성1이 식별속성)임을 표현하기 위해 관계선에 UID Bar를 그려줘야 한다.
3. 관계선을 반대로 그렸다. 관계선을 역으로 그린 후 엔터티2 속성1에 FK를 표시해야한다. 물론, 엔터티1의 속성1에서 FK는 제거해야 한다.

#

**# 데이터 모델 보기**

<img src="https://user-images.githubusercontent.com/66513003/119098500-dd6d2600-ba50-11eb-8b5e-a9d4607113ee.png" width="400">

- 1명의 쇼핑몰회원은 1명의 통합회원과 연결된다.
- 1명의 멤버쉽회원은 1명의 통합회원과 연결된다.
- 쇼핑몰회원과 멤버십회원은 반드시 통합회원과 연결되어야 한다.

- 통합회원이 쇼핑몰회원과 멤버십회원 중 어느 한 쪽에 `배타적으로` 연결되어야 한다고 정의하지 않았으므로 양쪽 회원에 모두 연결될 수 있다. 물론, 어느 한 쪽에만 연결될 수도 있다.

- 쇼핑몰회원과 멤버십회원 기준으로 볼 때 통합회원과 필수 관계(통합회원 쪽 관계선에 O표시가 없는 경우)이므로 쇼핑몰회원과 멤버십회원은 반드시 통합회원과 연결되어야 한다.

참고로,  아래는 애초에 회원을 통합한 데이터모델이다. 개념 모델 단계에서 회원을 통합설계하고 서브타입을 쇼핑몰회원과 멤버십회원으로 정의했다가 논리 모델 단계에서 필요(서브타입별 속성 정의, 관계 정의 등)에 의해 서브타입별 엔터티를 따로 설계한 것이다. 문제의 데이터 모델과 관계의 방향이 정반대인 점에서 주목하자. 즉, FK를 회원이 아닌 쇼핑몰 회원과 멤버쉽 회원 쪽에 정의하였다.

<img src="https://user-images.githubusercontent.com/66513003/119100202-aa2b9680-ba52-11eb-9a12-d32fb32aac23.png" width="400">

#

**# 부모 엔터티와 자식 엔터티가 비식별 관계를 가지는 데이터 모델**

<img src="https://user-images.githubusercontent.com/66513003/119100404-de9f5280-ba52-11eb-8c36-1b1002a44a98.png" width="400">

- 부모 엔터티의 식별자를 자식 엔터티의 식별자로 상속하면 `식별관계`, 일반속성으로 상속하면 `비식별관계`라고 한다. 식별, 비식별 관계를 표현하는 방식은 모델 표기법에 따라 다른데, 우선 바커(Barker) 표기법에서 두 엔터티를 식별관계로 정의하고자 할 때는 자식 쪽 관계선에 `UID Bar(수직 실선)`을 표시한다. UID Bar가 없으면 비식별 관계다.

#

**관계(Relationship)를 고려한 트랜잭션 구현**

- 트랜잭션은 일의 최소 단위이므로 하나의 트랜잭션으로 묶인 두 개 이상의 연산은 "동시에" 처리해야 한다. 현재의 저장 기술로는 동시 처리가 불가능하므로 DBMS는 트랜잭션의 원자서응ㄹ 지원하기 위해 'All or Nothing' 방식을 사용한다. 즉, 두 개 이상의 연산을 모두 성공하거나 모두 실패하도록 처리하는 방식을 사용한다.

- DB개발자는 원자적으로 처리해야 하는 일련의 작업을 하나의 트랙잭션으로 묶어주어야 하는데, 특히 관계가 설정된 두 개 이상 테이블에 데이터를 입력할 때 모델에 표현된 관계의 선택사양을 정확히 해석함으로써 정합성에 문제가 생기지 않도록 구현해야 한다.

- 자식 테이블 기준으로 부모 테이블이 `필수 관계`라면, 부모 레코드를 먼저 입력한 후에 자식 레코드를 입력해야 한다. 자식 레코드 입력 시, `외래 키에 부모의 식별자 값`을 반드시 입력해야 하기 때문이다. 부모 레코드 입력과 자식 레코드입력을 하나의 트랜잭션으로 묶어서 처리할 때는 순서만 잘 맞춰주면 된다. 두 연산을 개별 트랜잭션으로 처리했고 처리 순서도 보장할 수 없는 상황이라면, 자식 레코드를 입력할 때 부모 레코드가 `존재하는지 반드시 확인`해야 한다.

- 부모 엔터티 기준으로 자식 엔터티도 필수 관계라면, 부모와 자식 레코드 입력을 `한 트랙잭션`으로 묶어서 처리해야 한다. 부모 레코드 입력은 성공했는데 자식 레코드 입력은 실패하는 일이 생기면 안 되기 때문이다. 반드시 두 연산을 모두 성공하거나 모두 실패하도록 구현해야 한다. 부모 레코드와 함께 첫 번째 자식 레코드를 입력한 이후, 두 번째 자식 레코드부터는 개별적으로 입력할 수도 있는데, 이는 업무적인 트랜잭션 정의에 의해 결정된다.

#

주문과 주문상세의 인스턴스 생성을 하나의 트랜잭션에서 처리해야 하는 데이터 모델

<img src="https://user-images.githubusercontent.com/66513003/119214860-efa89c00-bb04-11eb-836d-dd5b1a1a8314.png" width="400">

- 위 데이터 모델은 주문은 반드시 주문상세가 있어야 하고, 주문상세는 반드시 주문이 있어야함을 나타낸다. 만약 주문처리와 주문상세처리를 각각 다른 트랜잭션으로 처리한다면, 특정 시점에는 주문이 없는 주문상세나 주문상세 없는 주문이 존재할 수도 있다. 따라서 위와 같은 데이터 발생 규칙을 만족하기 위해서는 하나의 트랜잭션에서 주문과 주문상세를 모두 처리해야 한다.

- 관계를 나타내는 막대에 O 표시가 있는 것은 두 데이터가 선택관계란 뜻이므로 하나의 트랙잭션에서 처리가 되지 않아도 된다.

#

**Null 속성**

- Null 값을 포함한 연산 결과는 항상 NULL이다.
    - 123 + NULL = NULL

- 연산 과정에 NULL값이 나타날 수 있다면 NULL을 특정 값으로 변환해주는 `NVL함수`를 같이 사용해야 한다. 값이 NULL인지 여부를 확인하고 싶을 때는 항상 `IS NULL` 조건식을 사용해야 한다. `'=', '<>', IN, NOT IN` 등의 연산자로는 원하는 결과를 얻을 수 없다.

- 컬럼 간 연산할 때 NULL이 포함되면 항상 NULL을 반환하지만, 여러 행 간에 `NUM, AVG, MIN, MAX, COUNT` 함수로 값을 집계할 때는 함수 인자 값이 NULL인 행이 포함되어도 결과를 정상적으로 반환한다. 여러 행을 읽어 값을 집계할 때는 NULL 값을 연산 대상에서 `제외`하기 때문이다.

#

부서별 연봉 계산

```sql
1.
SUM((급여 * 12) + NVL(수당, 0))

2.
(SUM(급여) * 12) + SUM (NVL (수당, 0))

3.
(SUM(급여 * 12)) + NVL(SUM(수당), 0)
```
- 셋 다 정확한 결과를 출력하지만, 급여 계산 및 NVL 함수 수행 횟수에 차이가 있다.

1. 급여에 대한 곱하기 연산과 수당에 대한 NVL함수를 사원별로 한 번씩 수행한다.
2. 급여에 대한 곱하기 연산은 부서별로, 수당에 대한 NVL 함수는 사원별로 한 번씩 수행한다. 
    - SUM함수와 같이 `여러 행의 값을 계산하는 함수`는 NULL이 포함되어도 `계산에서 알아서 제외되며` 나머지 값들의 계산 결과를 정상적으로 반환한다.
3. 급여에 대한 곱하기 연산과 수당에 대한 NVL 함수를 부서별로 한 번씩만 수행한다.

- 따라서 3번 표현식이 가장 효율적이다.

#

23(4)232  

**# 2 정규화**

<img src="https://user-images.githubusercontent.com/66513003/119216231-909b5500-bb0d-11eb-90fc-f7782ea920f5.png" width="400">

#

**# 계증형 데이터 모델**

- 일반적인 관계는 두 엔터티 간에 존재한다. 하지만, 한 엔터티에 속한 인스턴스끼리 관계가 존재하는 경우도 있는데, 이를 계층관계라고 한다. 순환관계, 자기참조관계, 재귀관계라고도 하며, 화면 메뉴, 조직도 등을 설계할 때 주로 사용한다.

- 상품분류를 예로 들어보자. 모든 상품을 대, 중, 소 3단계로 분류한다면, 상품대분류, 상품중분류, 상품소분류 엔터티를 따로 도출해서 이들 간의 관계를 설정해도 된다. 하지만, 상품마다 분류 단계가 다르고 단계의 깊이도 고정적이지 않다면(4단계 이상으로 늘어날 수 있다면), 상품 분류 엔터티 하나만 도출해서 계층관계로 설계해야 모델이 단순해지고 확장성 측면에서 유리하다.

- 계층관계는 일반적으로 양쪽 선택관계(Fully Optional)이다.

#

<img src="https://user-images.githubusercontent.com/66513003/119216535-300d1780-bb0f-11eb-945a-732161af9522.png" width="400">

- 사원은 고유한 사번이 부여된다.
- 사원은 담당 관리자가 1명 있을 수 있다.
- 사원은 다른 사원들의 관리자가 될 수 있다.

<img src="https://user-images.githubusercontent.com/66513003/119216646-d0633c00-bb0f-11eb-93c2-2375fec41b6e.png
" width="200">

- 사원 인스턴스 간에 관계가 존재하므로 계층 관계다. "담당 관리자가 1명 있을 수 있다."는 표현해서 담당 관리자가 없을 수도 있고, 있다면 1명이라는 사실을 알 수 있다. 즉, 사원 입장에서 상위관리자는 `선택 관계`다. "사원이 다른 사원<span style="color:#FF0000">들</span>의 관리자가 될 수 있다"고 했으므로 상위 관리자와 사원 간의 관계차수(Cardinality)는 1:M 선택 관계다. 문제에서 제시한 업무를 데이터 모델로 표현하려면, 순환(=자기참조) 방식으로 `1:M`관계선을 그리고, 관계선 양쪽에 O기호를 붙이면 된다.

#

- 트랜잭션의 특성

| 특징 | 설명 |
|---|---|
|원자성|트랜잭션의 작업은 모두 수행되거나 모두 수행되지 않아야 함|
|일관성|트랜잭션이 완료되면 데이터 무결성이 일관되게 보장되어야 함|
|고립성|트랜잭션이 다른 트랜잭션으로부터 고립된 상태로 수행되어야 함|
|지속성|트랜잭션이 완료되면 장애가 발생하더라도 변경 내용이 지속되어야 함|

#

<img src="https://user-images.githubusercontent.com/66513003/119217210-9f850600-bb13-11eb-94d1-e91e39fe3579.png
" width="200">

[SQL]
```sql
SELECT 부서번호, AVG (수당) AS 평균수당 FROM 사원 GROUP BY 부서번호
```
와 동일한 Query는?

```sql
1. 
SELECT 부서번호, SUM (수당) / COUNT(*) AS 평균수당 FROM 사원 GROUP BY 부서번호

2.
SELECT 부서번호, SUM (수당) / COUNT(수당) AS 평균수당 FROM 사원 GROUP BY 부서번호

3.
SELECT 부서번호, SUM (수당) / COUNT(NVL(수당, 0)) AS 평균수당 FROM 사원 GROUP BY 부서번호

4.
SELECT 부서번호, SUM (NVL(수당, 0) / COUNT(수당) AS 평균수당 FROM 사원 GROUP BY 부서번호
```

1. SUM(수당)은 부서별로 "수당에 NULL인 레코드를 제외한" 수당의 합을 구하지만, COUNT(*)는 부서별 "총" 사원 수를 구하므로 다르다.

**2. SUM(수당)과 COUNT(수당) 둘 다 수당이 NULL인 레코드를 제외하고 값을 구하므로 동일하다.**

3. COUNT(NVL(수당, 0))은 수당이 NULL인 레코드를 0으로 변환함으로써 부서별 총 사원수를 구하게 되므로 다르다.

4. COUNT(수당)은 부서별로 "수당이 NULL인 레코드를 제외한" 사원 수를 구한다. SUM(수당)과 SUM(NVL(수당, 0))은 결과가 같다. 수당이 NULL인 레코드를 제외하고 합을 구하든, 0으로 변환해서 합을 구하든 값이 같기 때문.

- 부서원의 수당이 모두 NULL인 부서는 결과가 달라지므로 주의해야 한다. 부서원의 수당이 모두 NULL인 경우 SUM(수당)은 NULL을 반환하고, SUM(NVL(수당, 0))은 0을 반환한다. 부서원의 수당이 모두 NULL이더라도 COUNT는 NULL을 반환하지 않고 0을 반환한다. NULL을 0으로 나누면 NULL을 반환하지만, NULL이 아닌 값을 0으로 나누면 에러가 발생한다. 결국, SUM(NVL(수당, 0)) 결과가 0일 때는 COUNT(수당)도 0이므로 에러가 발생한다.

#