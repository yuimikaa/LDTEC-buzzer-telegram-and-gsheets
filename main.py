#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <ESP8266HTTPClient.h>
#include <UniversalTelegramBot.h>

// Wi-Fi Credentials
const char* ssid = "DLink5G-244A";
const char* password = "D06cdf8996";

// Telegram Bot Credentials
const char* botToken = "YOUR_TELEGRAM_BOT_TOKEN";
const String chatID = "YOUR_TELEGRAM_CHAT_ID";

// Light Sensor Pin
#define LIGHT_SENSOR_PIN A0  // Analog pin for MH Light Sensor

// Google Form URL
const String form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfDd6iS2fdrZGoplZcmpQcx1uPxzt_fmdJW0znIc9ZoVC1NWQ/formResponse?usp=pp_url&entry.1309902686=";

// Secure WiFi Client
WiFiClientSecure secureClient;
UniversalTelegramBot bot(botToken, secureClient);

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    Serial.print("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.print(".");
    }
    Serial.println("\nConnected to WiFi!");

    // For both HTTPS requests (Google Form + Telegram)
    secureClient.setInsecure();
}

void loop() {
    int lightValue = analogRead(LIGHT_SENSOR_PIN);
    Serial.print("Light Sensor Value: ");
    Serial.println(lightValue);

    // === 1. Send to Google Form ===
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        String finalURL = form_url + String(lightValue) + "&submit=Submit";
        http.begin(secureClient, finalURL);

        int httpCode = http.GET();
        if (httpCode > 0) {
            Serial.println("✅ Data sent to Google Form!");
        } else {
            Serial.print("❌ Google Form failed. HTTP code: ");
            Serial.println(httpCode);
        }
        http.end();
    } else {
        Serial.println("⚠️ WiFi not connected!");
    }

    // === 2. Send Telegram Message ===
    String message = "📤 Light Sensor Report\n";
    message += "🔆 Intensity: " + String(lightValue) + "\n";
    message += "📅 Time: " + String(millis() / 1000) + "s since start";

    bot.sendMessage(chatID, message, "");

    delay(5000);  // Run every 5 seconds
}
while True:
        distance = get_distance()
        
        if distance > 0:
            print (Distance: {:2f} cm".format(distance))
            BUZZER_PIN.on() if distance (5 else BUZZER_PIN.off()
    else:
        print ("Error reading distance")
    
    time.sleep (0.2)
                                         
    try:
        h = {'content-type'} 'application' x-www-form-urlencoded}
    form_url="https://docs.google.com/forms/d/e/1FAIpQLSep1-EFfmOK24_jHm3t9mHjfJnMZJPh6a_NykPDAoT-iaatxA/formResponse?usp=
    form_data='entry.1257751470' + s+r (dstn)
    r = urequests.post (form url.data=form data.headers=H)
    print("Response code:"r.status_code")
    r.close()
    print ("submitted to google form")
except expection as e:
    print ("error submitting to form:",e)
    
    time.sleep (10)
