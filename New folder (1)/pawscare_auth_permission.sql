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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add comment gallery',7,'add_commentgallery'),(26,'Can change comment gallery',7,'change_commentgallery'),(27,'Can delete comment gallery',7,'delete_commentgallery'),(28,'Can view comment gallery',7,'view_commentgallery'),(29,'Can add page',8,'add_page'),(30,'Can change page',8,'change_page'),(31,'Can delete page',8,'delete_page'),(32,'Can view page',8,'view_page'),(33,'Can add reply',9,'add_reply'),(34,'Can change reply',9,'change_reply'),(35,'Can delete reply',9,'delete_reply'),(36,'Can view reply',9,'view_reply'),(37,'Can add gallery image',10,'add_galleryimage'),(38,'Can change gallery image',10,'change_galleryimage'),(39,'Can delete gallery image',10,'delete_galleryimage'),(40,'Can view gallery image',10,'view_galleryimage'),(41,'Can add message',11,'add_message'),(42,'Can change message',11,'change_message'),(43,'Can delete message',11,'delete_message'),(44,'Can view message',11,'view_message'),(45,'Can add customer',12,'add_customer'),(46,'Can change customer',12,'change_customer'),(47,'Can delete customer',12,'delete_customer'),(48,'Can view customer',12,'view_customer'),(49,'Can add register',13,'add_register'),(50,'Can change register',13,'change_register'),(51,'Can delete register',13,'delete_register'),(52,'Can view register',13,'view_register'),(53,'Can add tag',14,'add_tag'),(54,'Can change tag',14,'change_tag'),(55,'Can delete tag',14,'delete_tag'),(56,'Can view tag',14,'view_tag'),(57,'Can add product',15,'add_product'),(58,'Can change product',15,'change_product'),(59,'Can delete product',15,'delete_product'),(60,'Can view product',15,'view_product'),(61,'Can add order',16,'add_order'),(62,'Can change order',16,'change_order'),(63,'Can delete order',16,'delete_order'),(64,'Can view order',16,'view_order'),(65,'Can add my club user',17,'add_myclubuser'),(66,'Can change my club user',17,'change_myclubuser'),(67,'Can delete my club user',17,'delete_myclubuser'),(68,'Can view my club user',17,'view_myclubuser'),(69,'Can add venue',18,'add_venue'),(70,'Can change venue',18,'change_venue'),(71,'Can delete venue',18,'delete_venue'),(72,'Can view venue',18,'view_venue'),(73,'Can add event',19,'add_event'),(74,'Can change event',19,'change_event'),(75,'Can delete event',19,'delete_event'),(76,'Can view event',19,'view_event'),(77,'Can add patient',20,'add_patient'),(78,'Can change patient',20,'change_patient'),(79,'Can delete patient',20,'delete_patient'),(80,'Can view patient',20,'view_patient'),(81,'Can add appointment',21,'add_appointment'),(82,'Can change appointment',21,'change_appointment'),(83,'Can delete appointment',21,'delete_appointment'),(84,'Can view appointment',21,'view_appointment'),(85,'Can add profile',22,'add_profile'),(86,'Can change profile',22,'change_profile'),(87,'Can delete profile',22,'delete_profile'),(88,'Can view profile',22,'view_profile'),(89,'Can add post',23,'add_post'),(90,'Can change post',23,'change_post'),(91,'Can delete post',23,'delete_post'),(92,'Can view post',23,'view_post'),(93,'Can add comment',24,'add_comment'),(94,'Can change comment',24,'change_comment'),(95,'Can delete comment',24,'delete_comment'),(96,'Can view comment',24,'view_comment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
