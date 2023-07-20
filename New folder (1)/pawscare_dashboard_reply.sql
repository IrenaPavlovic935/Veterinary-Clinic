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
-- Table structure for table `dashboard_reply`
--

DROP TABLE IF EXISTS `dashboard_reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dashboard_reply` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `body` longtext NOT NULL,
  `date_added` datetime(6) NOT NULL,
  `comment_id` bigint NOT NULL,
  `parent_reply_id` bigint DEFAULT NULL,
  `replied_to_id` bigint DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dashboard_reply_comment_id_e7213f20_fk_dashboard` (`comment_id`),
  KEY `dashboard_reply_parent_reply_id_65b59f76_fk_dashboard_reply_id` (`parent_reply_id`),
  KEY `dashboard_reply_replied_to_id_d4dbf2e8_fk_dashboard_reply_id` (`replied_to_id`),
  KEY `dashboard_reply_user_id_5ec93d0f_fk_auth_user_id` (`user_id`),
  CONSTRAINT `dashboard_reply_comment_id_e7213f20_fk_dashboard` FOREIGN KEY (`comment_id`) REFERENCES `dashboard_commentgallery` (`id`),
  CONSTRAINT `dashboard_reply_parent_reply_id_65b59f76_fk_dashboard_reply_id` FOREIGN KEY (`parent_reply_id`) REFERENCES `dashboard_reply` (`id`),
  CONSTRAINT `dashboard_reply_replied_to_id_d4dbf2e8_fk_dashboard_reply_id` FOREIGN KEY (`replied_to_id`) REFERENCES `dashboard_reply` (`id`),
  CONSTRAINT `dashboard_reply_user_id_5ec93d0f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_reply`
--

LOCK TABLES `dashboard_reply` WRITE;
/*!40000 ALTER TABLE `dashboard_reply` DISABLE KEYS */;
INSERT INTO `dashboard_reply` VALUES (21,'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.','2023-07-19 09:33:57.839481',14,NULL,NULL,25),(22,'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.','2023-07-19 09:34:20.863793',14,21,NULL,1);
/*!40000 ALTER TABLE `dashboard_reply` ENABLE KEYS */;
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
