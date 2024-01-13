-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 13, 2024 at 03:32 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411267`
--

-- --------------------------------------------------------

--
-- Table structure for table `indeks`
--

CREATE TABLE `indeks` (
  `kode_komik` int(20) NOT NULL,
  `nama_komik` varchar(50) NOT NULL,
  `jenis_komik` varchar(50) NOT NULL,
  `penulis` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `indeks`
--

INSERT INTO `indeks` (`kode_komik`, `nama_komik`, `jenis_komik`, `penulis`, `penerbit`) VALUES
(1, 'Im reincarnated as indonesian cat', 'manhwa', 'Kim so gok', 'Milidia'),
(2, 'Strongest blackman', 'manga', 'Kimi wa syahrul', 'Milidia'),
(3, 'Kopi Idaman', 'Manhua', 'dimas ngopi', 'milidia'),
(4, '98 century boys', 'manga', 'aurell', 'ching media'),
(5, '1001 cara login FF', 'panduan', 'evos jeki', 'pochinok'),
(7, 'elf mabur', 'manga', 'johan', 'koles');

-- --------------------------------------------------------

--
-- Table structure for table `penjualan`
--

CREATE TABLE `penjualan` (
  `kode_komik` int(20) NOT NULL,
  `harga_komik` int(50) NOT NULL,
  `stok_komik` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `penjualan`
--

INSERT INTO `penjualan` (`kode_komik`, `harga_komik`, `stok_komik`) VALUES
(1, 80000, '12'),
(2, 40000, '40'),
(3, 60000, '15'),
(4, 98000, '10'),
(5, 15000, '90'),
(6, 120000, '7');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `indeks`
--
ALTER TABLE `indeks`
  ADD PRIMARY KEY (`kode_komik`);

--
-- Indexes for table `penjualan`
--
ALTER TABLE `penjualan`
  ADD PRIMARY KEY (`kode_komik`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `indeks`
--
ALTER TABLE `indeks`
  MODIFY `kode_komik` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `penjualan`
--
ALTER TABLE `penjualan`
  MODIFY `kode_komik` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
