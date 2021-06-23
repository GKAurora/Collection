package com.huawei.c4test.controller;

import com.huawei.c4test.configure.RestTemplateConfig;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.security.KeyManagementException;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("auth")
@CrossOrigin
public class LoginController {

    @RequestMapping(value = "get_token", method = RequestMethod.GET)
    public String getToken() throws NoSuchAlgorithmException, KeyStoreException, KeyManagementException {

        RestTemplate restTemplate = new RestTemplate(RestTemplateConfig.generateHttpRequestFactory());
        String url = "https://117.78.31.209:26335/rest/plat/smapp/v1/oauth/token";

        Map<String, String> map = new HashMap<>();
        map.put("grantType", "password");
        map.put("userName", "");
        map.put("value", "");

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.valueOf(MediaType.APPLICATION_JSON_VALUE));

        HttpEntity entity = new HttpEntity(map, headers);

        ResponseEntity<String> exchange = restTemplate.exchange(url, HttpMethod.PUT, entity, String.class);

        String body = exchange.getBody();
        System.out.println(body);

        return body;

    }



}
