-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2024 at 09:11 PM
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
(21, 'Villa Tranquil Haven', '123 Serenity Lane, Blissful City', 2, 1000000000, 'Escape to the tranquility of Villa Tranquil Haven, nestled in the heart of Blissful City. This serene retreat offers breathtaking views, modern amenities, and a perfect blend of comfort and elegance.', '2024-01-08 19:51:28', NULL, NULL),
(22, 'Harborview Residences', '456 Oceanfront Drive, Coastal Haven', 4, 2000000000, 'Harborview Residences, located on the picturesque Coastal Haven, redefine coastal living. Enjoy stunning ocean views, convenient access to the harbor, and a luxurious lifestyle.', '2024-01-08 19:52:50', NULL, NULL),
(23, 'Meadowside Apartments', '789 Green Meadows Blvd, Nature', 3, 4000000000, 'Discover the beauty of Meadowside Apartments in the heart of Nature\'s Crossing. Surrounded by green meadows, these apartments offer a peaceful retreat with modern conveniences.', '2024-01-08 19:53:37', NULL, NULL);

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
(24, 22, 'frames-for-your-heart-2d4lAQAlbDA-unsplash.jpg', NULL, NULL, NULL),
(25, 23, 'r-architecture-T6d96Qrb5MY-unsplash.jpg', NULL, NULL, NULL),
(26, 23, 'r-architecture-JvQ0Q5IkeMM-unsplash.jpg', NULL, NULL, NULL),
(27, 21, 'r-architecture-2gDwlIim3Uw-unsplash.jpg', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` int(50) NOT NULL,
  `image_name` varchar(200) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `meet_date` varchar(50) DEFAULT NULL,
  `payment` varchar(100) NOT NULL DEFAULT 'PAY ON THE SPOT',
  `total_price` float NOT NULL,
  `status` varchar(100) NOT NULL DEFAULT 'PENDING',
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`id`, `image_name`, `user_name`, `meet_date`, `payment`, `total_price`, `status`, `created_at`, `updated_at`) VALUES
(6, 'frames-for-your-heart-2d4lAQAlbDA-unsplash.jpg', 'admin', '2024-01-12', 'PAY ON THE SPOT', 2000000000, 'PENDING', '2024-01-08 19:55:48', NULL);

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
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `property_category`
--
ALTER TABLE `property_category`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `property_galleries`
--
ALTER TABLE `property_galleries`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
