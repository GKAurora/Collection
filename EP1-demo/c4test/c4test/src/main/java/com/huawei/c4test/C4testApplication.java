package com.huawei.c4test;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication(exclude= {DataSourceAutoConfiguration.class})
public class C4testApplication {

	public static void main(String[] args) {
		SpringApplication.run(C4testApplication.class, args);
	}



}
