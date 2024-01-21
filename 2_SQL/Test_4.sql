CREATE TABLE Submissions_1 (
    Deal_id INT PRIMARY KEY,
    LoanAmount INT,
    interest_rate DECIMAL(5, 2),
    rate_type VARCHAR(20)
);

INSERT INTO Submissions_1 (Deal_id, LoanAmount, interest_rate, rate_type)
VALUES
    (1, 10000, 8.75, 'variable'),
    (100, 10000, 11.37, 'fixed'),
    (1010, 15000, 8.25, 'fixed'),
    (1051, 20000, 4.75, 'variable'),
    (1251, 40000, 4.75, 'variable'),
    (130, 10000, 3.00, 'variable');

SELECT * FROM Submissions_1



CREATE TABLE Loans_1 (
    Deal_id INT PRIMARY KEY,
    Merchant_Id INT,
    Funded_date DATE,
    Industry_type VARCHAR(20)
);

INSERT INTO Loans_1 (Deal_id, Merchant_Id, Funded_date, Industry_type)
VALUES
    (1, 1, '2016-01-01', 'New'),
    (100, 80, '2016-04-01', 'New'),
    (130, 100, '2016-04-15', 'New'),
    (1010, 1, '2017-06-23', 'Renewal'),
    (1051, 100, '2017-07-01', 'Renewal'),
    (1251, 1, '2017-10-01', 'Renewal');

Select * from Loans_1


SELECT
  l.Merchant_Id,
  l.Deal_id,
  s.LoanAmount 
FROM Loans_1 l
JOIN Submissions_1 s 
ON l.Deal_id = s.Deal_id
WHERE l.Industry_type = 'Renewal'
AND l.Funded_date = (
  SELECT MAX(Funded_date)
  FROM Loans_1
  WHERE Merchant_Id = l.Merchant_Id
  AND Industry_type = 'Renewal'
);