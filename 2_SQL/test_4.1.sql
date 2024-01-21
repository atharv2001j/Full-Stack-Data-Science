CREATE TABLE Loans (
    Deal_id INT,
    Merchant_Id INT,
    Funded_date DATE,
    Industry VARCHAR(255),
	Type varchar(455)
)

INSERT INTO Loans 
VALUES
    (1, 1, '2016-01-01', 'Retail', 'New'),
    (100, 80, '2016-04-01', 'Construction', 'New'),
    (130, 100, '2016-04-15', 'Trucking',  'New'),
    (1010, 1, '2017-06-23', 'Retail' ,'Renewal'),
    (1051, 100, '2017-07-01', 'Trucking' ,'Renewal'),
    (1251, 1, '2017-10-01', 'Retail', 'Renewal');

SELECT * FROM Loans

CREATE TABLE Submissions (
    Deal_id INT,
    Loan_Amount DECIMAL(10, 2),
    Interest_Rate DECIMAL(5, 2),
    Rate_Type VARCHAR(255)
);


INSERT INTO Submissions (Deal_id, Loan_Amount, Interest_Rate, Rate_Type)VALUES
(1, 10000.00, 8.75, 'variable'),
    (100, 10000.00, 11.37, 'fixed'),
    (1010, 15000.00, 8.25, 'fixed'),
    (1051, 20000.00, 4.75, 'variable'),
    (1251, 40000.00, 4.75, 'variable'),
    (130, 10000.00, 3.00, 'variable');

SELECT * FROM Submissions


SELECT
  l.Merchant_Id,
  l.Deal_id,
  s.Loan_Amount 
FROM Loans l
JOIN Submissions s 
ON l.Deal_id = s.Deal_id
WHERE l.Industry = 'Renewal'
AND l.Funded_date = (
  SELECT MAX(Funded_date)
  FROM Loans
  WHERE Merchant_Id = l.Merchant_Id
  AND Industry = 'Renewal'
);