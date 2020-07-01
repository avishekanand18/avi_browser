-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 01, 2020 at 04:42 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `avi_browser`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookmarks`
--

CREATE TABLE `bookmarks` (
  `email` varchar(30) NOT NULL,
  `u_book` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookmarks`
--

INSERT INTO `bookmarks` (`email`, `u_book`) VALUES
('avi@hit', 'https://www.facebook.com/');

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `email` varchar(30) NOT NULL,
  `u_hist` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`email`, `u_hist`) VALUES
('avi@hit', 'https://www.google.com/'),
('avi@hit', 'https://www.facebook.com/'),
('avi@hit', 'https://www.google.com/'),
('avi@hit', 'https://www.facebook.com/'),
('avi@hit', 'https://www.google.com/'),
('avi@hit', 'https://www.facebook.com/'),
('avi@hit', 'https://www.google.com/'),
('avi@hit', 'https://www.google.com/search?source=hp&ei=01_oXqy_F4rfrQGSq5TIBA&q=ghfjj&oq=ghfjj&gs_lcp=CgZwc3ktYW'),
('avi@hit', 'https://www.hackerearth.com/@ghfjj'),
('avi@hit', 'https://www.google.com/search?source=hp&ei=01_oXqy_F4rfrQGSq5TIBA&q=ghfjj&oq=ghfjj&gs_lcp=CgZwc3ktYW'),
('avi@hit', 'https://www.google.com/search?ei=3V_oXtCYFJvorQGdzrx4&q=ubuntu&oq=ubunto&gs_lcp=CgZwc3ktYWIQARgAMgQI'),
('avi@hit', 'https://ubuntu.com/');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `email` varchar(50) NOT NULL,
  `psw` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`email`, `psw`) VALUES
('avi@hit', 'avi123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD UNIQUE KEY `email` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
