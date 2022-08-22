### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select * from playlist_track as A order by A.playlistId desc limit 5;
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select * from tracks as B order by b.TrackId limit 5;
``` 
 
### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
Column A | Column B | Column C
---------|----------|---------
 A1 | B1 | C1
 A2 | B2 | C2
 A3 | B3 | C3


```sql
select PlaylistId, Name from playlist_track A inner join tracks B on A.TrackId = B.TrackId order by PlaylistId desc limit 10;
```  

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select PlaylistId, Name from playlist_track A inner join tracks B on A.TrackId = B.TrackId where PlaylistId = 10 order by Name desc limit 5;
``` 

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
select count(*) from tracks A inner join artists B on A.Composer = B.Name;
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
select count(*) from tracks A left join artists B on A.Composer = B.Name;
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
inner join은 두 테이블 간의 교집합 즉 서로 속해있는 것만 추출하고,
left join은 한쪽의 테이블은 모두 포함하고 서로 가지고 있는 부분에서 포함되어 있지 않은 부분은 제외 시키기 때문에 left join을 하면 서로 가지고 있는 값 + 양쪽 테이블 중 하나의 테이블에 속한 값들을 모두 추출하기 때문에 양 테이블 값이 완벽하게 같지 않는 이상 left join이 inner join보다 값이 많을 수 밖에 없다
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select InvoiceLineId, InvoiceId from invoice_items order by InvoiceId limit 5;
``` 

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select InvoiceId, CustomerId from invoices order by InvoiceId limit 5;
``` 

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select InvoiceLineId, InvoiceId from invoice_items inner join invoices on invoice_items.InvoiceId = invoices.InvoiceId order by InvoiceId desc limit 5;
-- 여기서 막힘
``` 


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```

``` 

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```

```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql

```

