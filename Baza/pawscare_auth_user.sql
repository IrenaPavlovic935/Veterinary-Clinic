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
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$dizM2bsNUcmLNJdugkPFMQ$8Q5hOGSbHv8bbv23rH1SgNCBGW+0lPA30ckegJuriWU=','2023-07-19 15:59:23.441483',1,'Irena_Pavlovic','','','Irena@gmail.com',1,1,'2023-06-30 11:05:44.290725'),(25,'pbkdf2_sha256$390000$qrSbPOkdWVRhcjwcEGYSSH$eKON39KbdLFAVXVfe1CzuRQH9g+6ndcB7ksHLogUyLU=','2023-07-19 09:33:48.411644',0,'Amraa_Halabaa','Amra','Halaba','amra@gmail.com',0,1,'2023-07-18 20:15:21.746704'),(26,'pbkdf2_sha256$390000$CPk26qYnW7MsgE8Ynike1l$hyzHhgK3MQD6W19wqy8Lcyb8EYI0UjGPGTSunJ+X6Q4=','2023-07-18 20:43:11.997171',0,'Lejlaa_Kehic','lejla','kehic','Lejlaa.Kehic@gmail.com',0,1,'2023-07-18 20:43:10.668521'),(27,'pbkdf2_sha256$390000$uumniv2HqVfFksBVVn5DA5$AWkXUb94gkZ/kTdCeIuGXUDbqPlF43S9vHY+hkQw3tI=','2023-07-19 11:29:21.271341',0,'adexx','adnan','kepes','adex@gmail.com',0,1,'2023-07-19 11:29:20.678516'),(28,'pbkdf2_sha256$390000$wcf68I1uuJQE8rsc8nwkQO$AMdNR9NDDJ47tggwV/R817I6S+Gj2DCae/39RgMD8Q8=','2023-07-19 16:09:16.596272',0,'Emir_Puska','Emir','Puska','Emir_Puska@gmail.com',0,1,'2023-07-19 16:09:15.338810');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
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
