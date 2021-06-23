package com.huawei.c4test.controller;

import com.huawei.c4test.configure.RestTemplateConfig;
import net.minidev.json.JSONArray;
import net.minidev.json.JSONObject;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.http.client.ClientHttpResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.DefaultResponseErrorHandler;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.security.KeyManagementException;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.util.LinkedHashMap;
import java.util.List;

@RestController
@RequestMapping("heartmap")
@CrossOrigin
public class HeartMapController {

    @RequestMapping(value = "get_heartmap", method = RequestMethod.GET)
    public String getHeartMap(@RequestParam(value = "id", required=false) String id) throws NoSuchAlgorithmException, KeyStoreException, KeyManagementException {


        RestTemplate restTemplate = new RestTemplate(RestTemplateConfig.generateHttpRequestFactory());
        restTemplate.setErrorHandler(new DefaultResponseErrorHandler(){
            @Override
            public void handleError(ClientHttpResponse response) throws IOException {
                if(response.getRawStatusCode() != 401){
                    super.handleError(response);
                }
            }
        });

        String url = "https://117.78.31.209:26335/rest/campusrtlswebsite/v1/clientlocation/heatmap";

        String tokenURL = "http://localhost:8080/auth/get_token";
        JSONObject resultJson = restTemplate.getForObject(tokenURL, JSONObject.class);
        if(resultJson.get("accessSession") == null){
            return "FAIL";
        };
        String token = (String) resultJson.get("accessSession");

        System.out.println(token);

        // 热力图请求
        HttpHeaders headers = new HttpHeaders();

        headers.add("Content-Type", "application/json");
        headers.add("Accept", "application/json");
        headers.add("X-Auth-Token", token);
//        headers.add("id", "/");

        HttpEntity entity = new HttpEntity(null, headers);
        url = url+"?startTime=1624323600000&endTime=1624327200000";
        ResponseEntity<JSONObject> resJson = restTemplate.exchange(url, HttpMethod.POST, entity, JSONObject.class);

        System.out.println(resJson.getBody());
        List list = (List) resJson.getBody().get("data");
        System.out.println(list);
        JSONArray jsonArray = new JSONArray();
        for(int i = 0; i < list.size(); i++){
            JSONObject jo = new JSONObject();
            LinkedHashMap map = new LinkedHashMap();
            map = (LinkedHashMap) list.get(i);
            //数据缩放按照自己的方式来，这里只是简单的缩放
            int count  = (int) map.get("count")/5000 * 50;
            jo.put("x", map.get("x"));
            jo.put("y", map.get("y"));
            jo.put("value", count);
            jsonArray.add(jo);
        }



        return jsonArray.toString();

    }



}
