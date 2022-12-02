-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2022 at 06:57 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bmi`
--

-- --------------------------------------------------------

--
-- Table structure for table `bmicare`
--

CREATE TABLE `bmicare` (
  `bmiid` int(5) NOT NULL,
  `bmitype` varchar(255) NOT NULL,
  `bmicomment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bmicare`
--

INSERT INTO `bmicare` (`bmiid`, `bmitype`, `bmicomment`) VALUES
(1, 'underweight', 'you need to eat all five groups of food and go to see the doctor if it does not work'),
(2, 'normal', 'well done!! your bmi result is good.Keep on it.'),
(3, 'overweight', 'you have a little bit fat so you just need to do more workout'),
(4, 'obese', 'Your bmi is badly too much.You need a hard workout an food control'),
(5, 'extremely obese', 'You are dangerously fat.It can cause sebum embolism or something worse. You should exercise regularly and see a doctor urgently.');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
