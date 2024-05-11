-- 创建数据库
CREATE DATABASE IF NOT EXISTS rent;

-- 使用创建的数据库
USE rent;

-- 创建表结构
CREATE TABLE IF NOT EXISTS rent_customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(128) NOT NULL,
    avatar_url VARCHAR(512),
    wx_open_id VARCHAR(256),
    wx_session_key VARCHAR(256)
) AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS rent_expect (
    id INT AUTO_INCREMENT PRIMARY KEY,
    from_customer INT, 
    house_type VARCHAR(256), 
    price INT, 
    province_code INT,
    location TEXT,
    title VARCHAR(128) NOT NULL,
    content TEXT
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS rent_house (
    id INT AUTO_INCREMENT PRIMARY KEY,
    from_customer INT, 
    area_size INT,
    house_type VARCHAR(256), 
    price INT, 
    province_code INT,
    location TEXT,
    photo_list TEXT,
    title VARCHAR(128) NOT NULL,
    content TEXT,
    check_status INT
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS rent_house (
    id INT AUTO_INCREMENT PRIMARY KEY,
    from_customer INT, 
    title VARCHAR(128) NOT NULL,
    content TEXT
)AUTO_INCREMENT = 1;