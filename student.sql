-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 07, 2021 at 04:57 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student`
--

-- --------------------------------------------------------

--
-- Table structure for table `entry`
--

CREATE TABLE `entry` (
  `ID` int(11) NOT NULL,
  `ROLL_NUMBER` varchar(50) DEFAULT NULL,
  `NAME` varchar(50) DEFAULT NULL,
  `FATHER_NAME` varchar(50) DEFAULT NULL,
  `AGE` varchar(50) DEFAULT NULL,
  `SECTION` varchar(50) DEFAULT NULL,
  `ADDRESS` varchar(220) DEFAULT NULL,
  `MOBILE_NUMBER` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `entry`
--

INSERT INTO `entry` (`ID`, `ROLL_NUMBER`, `NAME`, `FATHER_NAME`, `AGE`, `SECTION`, `ADDRESS`, `MOBILE_NUMBER`) VALUES
(1, '96808106307', 'Er.Muthu Kumar', 'CHINTHAMANI', '32', 'B.E', '162', '7812069569'),
(2, '98989', 'Er.Muthu Kumar', 'CHINTHAMANI', '87', 'B.E', 'MADIPAKKAM BAZAR ROAD', '09789714771'),
(3, '96808106307', 'RAMYA SRI SAKTHI', 'SANKARALINGAM', '27', 'B.E', '4-3-7 AMBALAM STREET, PULIYARAI', '9790320449'),
(4, '90', 'RAMYA SRI', 'SANKARALINGAM', '32', 'B.TECH', 'PULIYARAI', '9790320449'),
(5, '999', 'muthukumar', 'chinthamani', '22', '10th ', 'kalugumalai', '909999898'),
(6, '676', 'bnbcn', 'jcvbj', '23', 'dfdf', 'dsd', '0909');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('a', 'a'),
('muthukumar', 'muthukumar'),
('admin', 'admin'),
('muthu', 'muthu'),
('ermuthu', 'admin'),
('muthukumar', 'muthu05514'),
('admin', 'root'),
('isunmuthu@gmail.com', 'admin'),
('isunmuthu@gmail.com', 'muthu'),
('a@gmail.com', 'a'),
('muthu@gmail.com', '123'),
('isun@gmail.com', 'z'),
('isunmuthu@gmail.com', 'a'),
('isunmuthu@gmail.com', 'q');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `entry`
--
ALTER TABLE `entry`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `entry`
--
ALTER TABLE `entry`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
