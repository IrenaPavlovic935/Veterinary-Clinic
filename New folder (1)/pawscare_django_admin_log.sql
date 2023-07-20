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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-07-05 13:01:55.291708','6','adex',3,'',4,1),(2,'2023-07-12 21:11:38.790438','15','Becirbasic',3,'',4,1),(3,'2023-07-13 09:54:31.672812','7','lidijaaaaaa_pavlovic',3,'',22,1),(4,'2023-07-13 09:57:24.437951','18','Lidijaaa.aa_P',3,'',4,1),(5,'2023-07-13 09:57:24.440554','8','lidijaaaaaa_pavlovic',3,'',4,1),(6,'2023-07-13 12:18:28.378770','9','Ivanaaa.aa_M',3,'',4,1),(7,'2023-07-13 12:18:28.382145','19','Lidijaaa.aa_P',3,'',4,1),(8,'2023-07-13 12:18:28.384192','5','Novakk.nn_N',3,'',4,1),(9,'2023-07-13 12:18:28.387487','20','Snezanaaa.aa_D',3,'',4,1),(10,'2023-07-13 12:20:22.890806','3','Amraa_Halabaa',3,'',4,1),(11,'2023-07-18 20:12:44.809568','25','VIKAA',3,'',22,1),(12,'2023-07-18 20:12:44.815470','8','adex',3,'',22,1),(13,'2023-07-18 20:26:41.214121','25','25',3,'',10,1),(14,'2023-07-18 20:26:41.217437','24','24',3,'',10,1),(15,'2023-07-18 20:26:41.219942','23','23',3,'',10,1),(16,'2023-07-18 20:26:41.223037','22','22',3,'',10,1),(17,'2023-07-18 20:26:41.225351','21','21',3,'',10,1),(18,'2023-07-18 20:26:41.227742','20','20',3,'',10,1),(19,'2023-07-18 20:26:41.231112','19','19',3,'',10,1),(20,'2023-07-18 20:26:41.233195','16','16',3,'',10,1),(21,'2023-07-18 20:26:41.235395','13','13',3,'',10,1),(22,'2023-07-18 20:26:41.238288','12','12',3,'',10,1),(23,'2023-07-18 20:26:41.240579','9','9',3,'',10,1),(24,'2023-07-18 20:26:41.243500','8','8',3,'',10,1),(25,'2023-07-18 20:26:41.245959','3','3',3,'',10,1),(26,'2023-07-19 10:28:45.312856','10','adex',3,'',4,1),(27,'2023-07-19 10:28:45.315720','4','amina',3,'',4,1),(28,'2023-07-19 10:28:45.317684','16','Becirbasic',3,'',4,1),(29,'2023-07-19 10:28:45.320313','23','VIKAA',3,'',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-20 10:33:33
