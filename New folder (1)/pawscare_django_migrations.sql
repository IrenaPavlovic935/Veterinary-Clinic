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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-06-30 11:05:04.645241'),(2,'auth','0001_initial','2023-06-30 11:05:04.957811'),(3,'admin','0001_initial','2023-06-30 11:05:05.054189'),(4,'admin','0002_logentry_remove_auto_add','2023-06-30 11:05:05.070154'),(5,'admin','0003_logentry_add_action_flag_choices','2023-06-30 11:05:05.082116'),(6,'appointment','0001_initial','2023-06-30 11:05:05.171800'),(7,'contenttypes','0002_remove_content_type_name','2023-06-30 11:05:05.232548'),(8,'auth','0002_alter_permission_name_max_length','2023-06-30 11:05:05.270630'),(9,'auth','0003_alter_user_email_max_length','2023-06-30 11:05:05.301312'),(10,'auth','0004_alter_user_username_opts','2023-06-30 11:05:05.311285'),(11,'auth','0005_alter_user_last_login_null','2023-06-30 11:05:05.354712'),(12,'auth','0006_require_contenttypes_0002','2023-06-30 11:05:05.357704'),(13,'auth','0007_alter_validators_add_error_messages','2023-06-30 11:05:05.368261'),(14,'auth','0008_alter_user_username_max_length','2023-06-30 11:05:05.412369'),(15,'auth','0009_alter_user_last_name_max_length','2023-06-30 11:05:05.457826'),(16,'auth','0010_alter_group_name_max_length','2023-06-30 11:05:05.482316'),(17,'auth','0011_update_proxy_permissions','2023-06-30 11:05:05.493281'),(18,'auth','0012_alter_user_first_name_max_length','2023-06-30 11:05:05.544177'),(19,'blog','0001_initial','2023-06-30 11:05:05.769962'),(20,'club','0001_initial','2023-06-30 11:05:05.973487'),(21,'club','0002_remove_event_attendees','2023-06-30 11:05:05.997424'),(22,'dashboard','0001_initial','2023-06-30 11:05:06.535999'),(23,'front','0001_initial','2023-06-30 11:05:06.617537'),(24,'sessions','0001_initial','2023-06-30 11:05:06.641291'),(25,'users','0001_initial','2023-06-30 11:05:06.850235'),(26,'dashboard','0002_delete_page','2023-07-13 11:35:20.318918'),(27,'users','0002_remove_order_customer_remove_order_product_and_more','2023-07-13 11:35:20.598810'),(28,'appointment','0002_alter_appointment_animal_age','2023-07-17 19:15:15.224824'),(29,'appointment','0003_alter_appointment_animal_age','2023-07-17 19:41:58.685571'),(30,'appointment','0004_remove_appointment_animal_age_patient_animal_age','2023-07-17 19:56:11.962332'),(31,'appointment','0005_remove_patient_animal_age_appointment_animal_age','2023-07-17 19:58:02.847562');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
