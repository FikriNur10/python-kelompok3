-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2024 at 05:22 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `property_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `properties`
--

CREATE TABLE `properties` (
  `id` int(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `category_id` int(50) NOT NULL,
  `price` double NOT NULL,
  `description` varchar(200) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `properties`
--

INSERT INTO `properties` (`id`, `name`, `address`, `category_id`, `price`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Villa Mas', 'Jl Budi Indah', 1, 200000, 'rumah ini sangat mahal', NULL, NULL, NULL),
(2, 'laserjump', 'Jl Alam Sutera', 2, 1000000000, 'RUmah jelek', NULL, NULL, NULL),
(3, 'laserjump', 'sdafasf', 2, 150000000, 'sdafsadfsadfda', NULL, NULL, NULL),
(4, 'laserjump', 'asdf', 2, 1500, 're', NULL, NULL, NULL),
(5, 'qwrewqe', 'qwerwe', 2, 324, 'ewqrwr', NULL, NULL, NULL),
(6, 'laserjump', 'qwer', 1, 231, 'wer', NULL, NULL, NULL),
(7, 'Davin', 'safdasdfsa', 1, 345, 'fghhgf', NULL, NULL, NULL),
(8, 'asdfasd', 'asdffasd', 1, 24312, 'fasf', NULL, NULL, NULL),
(9, 'laserjump', 'sadf', 2, 2134, 'dsfa', NULL, NULL, NULL),
(19, 'Davin', 'jl budi indah', 4, 999999, 'asfsfsafsafsdfsdafsadf', '2024-01-08 15:37:06', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `property_category`
--

CREATE TABLE `property_category` (
  `id` int(50) NOT NULL,
  `name` varchar(200) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `property_category`
--

INSERT INTO `property_category` (`id`, `name`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Single-Family Homes', NULL, NULL, NULL),
(2, 'Townhouses', NULL, NULL, NULL),
(3, 'Multi-Family Homes', NULL, NULL, NULL),
(4, 'Condominiums', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `property_galleries`
--

CREATE TABLE `property_galleries` (
  `id` int(50) NOT NULL,
  `property_id` int(50) NOT NULL,
  `name` varchar(200) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `property_galleries`
--

INSERT INTO `property_galleries` (`id`, `property_id`, `name`, `created_at`, `updated_at`, `deleted_at`) VALUES
(20, 19, '1_F3PttTE_aJbhJ9OIaBRHtg.jpeg', NULL, NULL, NULL),
(21, 19, '6d7e813e0a48e4a4ac98875cd6391eb2.jpg', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` int(50) NOT NULL,
  `image_name` varchar(200) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `payment` varchar(100) NOT NULL DEFAULT 'PAY ON THE SPOT',
  `total_price` float NOT NULL,
  `status` varchar(100) NOT NULL DEFAULT 'PENDING',
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`id`, `image_name`, `user_name`, `payment`, `total_price`, `status`, `created_at`, `updated_at`) VALUES
(4, '', 'admin', 'PAY ON THE SPOT', 2134, 'PENDING', '2024-01-07 18:34:40', NULL),
(5, '1_F3PttTE_aJbhJ9OIaBRHtg.jpeg', 'admin', 'PAY ON THE SPOT', 999999, 'PENDING', '2024-01-08 15:44:16', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `transaction_items`
--

CREATE TABLE `transaction_items` (
  `id` int(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `property_id` int(50) NOT NULL,
  `transaction_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction_items`
--

INSERT INTO `transaction_items` (`id`, `user_name`, `property_id`, `transaction_id`) VALUES
(4, 'admin', 9, 4);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(20) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` varchar(50) DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `fullname`, `email`, `username`, `password`, `role`) VALUES
(1, 'admin', 'admin@gmail.com', 'admin', 'admin', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `properties`
--
ALTER TABLE `properties`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_category`
--
ALTER TABLE `property_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_galleries`
--
ALTER TABLE `property_galleries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaction_items`
--
ALTER TABLE `transaction_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `properties`
--
ALTER TABLE `properties`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `property_category`
--
ALTER TABLE `property_category`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `property_galleries`
--
ALTER TABLE `property_galleries`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `transaction_items`
--
ALTER TABLE `transaction_items`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
