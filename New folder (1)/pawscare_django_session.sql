-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: pawscare
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('60oupwicfzcw0nszvdjonh4v8sc3tnpv','.eJxVjDsOwjAQBe_iGln-xD9Kes5gre1dHEC2FCcV4u4QKQW0b2bei0XY1hq3gUucCzsz5dnpd0yQH9h2Uu7Qbp3n3tZlTnxX-EEHv_aCz8vh_h1UGPVbS3QuAAYThHHCW6NlTjYQKTJAJSEZ4T1aAi0n8mAFqUnoXHwCraxm7w8Hpjgb:1qM9jo:w22FI-bQ2D8WAmrGeXwV-Jf6C8XxW_70qAKUPkH2OGg','2023-08-02 16:09:16.600402'),('k7nrejdut7sgi1npj9fts8l2zf19yv79','.eJxVjEEOwiAQRe_C2pABWgGX7nsGMsOAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERgzj9boTxkeoO-I711mRsdV1mkrsiD9rl1Dg9r4f7d1Cwl2-tiGImdJFMtiPjmSIYrzQBaKuztSoP3kKK3rBig0BsACyo5FweXRLvDwLCOB0:1qFKGZ:m5WjpyM1s97vVjlFjoSE_n04Op7iZR7Opv_FvhRQBoI','2023-07-14 19:58:51.578978'),('nfn3fo18pv3kttsulyu8f8d8bogh869f','.eJxVjEsOwjAMBe-SNYqcksQNS_Y9Q-XYLimgVOpnhbg7VOoCtm9m3sv0tK2l3xad-1HMxSRz-t0y8UPrDuRO9TZZnuo6j9nuij3oYrtJ9Hk93L-DQkv51o4CBMazS6IBHMUBYkICaT1KRAcxtqo-hdwwZhQmGGTwwIzehUbN-wPOhDel:1qIrEq:o155e3vbfSNSNNc2uOtgQ4SKeXux-2aopc0SVDp_n3I','2023-07-24 13:47:40.749121'),('qisworm8l35568a55c3cf8jv8smsqv2q','.eJxVjMEOwiAQBf-FsyFAYQGP3v0GArsgVQNJaU_Gf9cmPej1zcx7sRC3tYZt5CXMxM4M2Ol3SxEfue2A7rHdOsfe1mVOfFf4QQe_dsrPy-H-HdQ46rfWkMCj9tpQ1qWgoWJTVmCpYLICnZPSRS9JGJ-EBFWcQe0gkpokTp69P_dXN-s:1qFuNX:K9M5Xd_8DhNQojBdOZMqZB-v1jAK--K2dw_YU-JpOs8','2023-07-16 10:32:27.752926'),('tugu58bqdycv4zkkic20y6j66rwq0sk3','.eJxVjDsOwyAQBe9CHSEWm1_K9D4DWlgITiKQjF1FuXtsyUXSzsx7b-ZxW4vfelr8TOzKANjlFwaMz1QPQw-s98Zjq-syB34k_LSdT43S63a2fwcFe9nX2WlFOWU9ONAqYhJKGINg8yDIwLizMUVyEnRwFDJltFJKRCF0iFazzxcP7zhl:1qJAQD:BOdVlA_gBmz5oHGJH1Xn8uiiqydRDlK_FTIje3A8fq8','2023-07-25 10:16:41.909670'),('wc4l8bsbfzsj3gry4y9elusjabhmig2a','.eJxVjMsOwiAQRf-FtSEMbWFw6d5vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yjOAsTpd2MKj1R3EO9Ub02GVtdlZrkr8qBdXltMz8vh_h0U6uVbMySVcERAADfoHADRsDZOEaU4INowGgicnSU2UWc7BMc4keY4gbLi_QHSADeo:1qGbyK:M1RAPrkRExU3Esi2W6LBwIsjcRBJIL7pNEuif5CWbh8','2023-07-18 09:05:20.049571');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-20 10:33:32
