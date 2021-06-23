package com.huawei.c4test.controller;

import com.huawei.c4test.configure.RestTemplateConfig;
import net.minidev.json.JSONObject;
import org.springframework.http.*;
import org.springframework.http.client.ClientHttpResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.DefaultResponseErrorHandler;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.security.KeyManagementException;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("site")
@CrossOrigin
public class SiteController {

    @RequestMapping(value = "get_sites", method = RequestMethod.GET)
    public String getSite(@RequestParam(value = "id", required=false) String id) throws NoSuchAlgorithmException, KeyStoreException, KeyManagementException {


        RestTemplate restTemplate = new RestTemplate(RestTemplateConfig.generateHttpRequestFactory());
        restTemplate.setErrorHandler(new DefaultResponseErrorHandler(){
            @Override
            public void handleError(ClientHttpResponse response) throws IOException {
                if(response.getRawStatusCode() != 401){
                    super.handleError(response);
                }
            }
        });
        String url = "https://49.4.21.18:26335/rest/uninetwork-res/v1/position/subtree";

        String tokenURL = "http://localhost:8080/auth/get_token";
        JSONObject resultJson = restTemplate.getForObject(tokenURL, JSONObject.class);
        if(resultJson.get("accessSession") == null){
            return "FAIL";
        };
        String token = (String) resultJson.get("accessSession");

        System.out.println(token);
//
        HttpHeaders headers = new HttpHeaders();

        headers.add("Content-Type", "application/json");
        headers.add("Accept", "application/json");
        headers.add("X-Auth-Token", token);
        headers.add("id", "/");

        HttpEntity entity = new HttpEntity(null, headers);

        ResponseEntity<String> resJson = restTemplate.exchange(url, HttpMethod.GET, entity, String.class);

        System.out.println(resJson.getBody());

        return resJson.getBody();

    }



}
