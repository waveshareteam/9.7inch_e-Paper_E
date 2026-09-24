#include "EPD_9in7e.h"
#include "GUI_Paint.h"
#include "fonts.h"
#include "ImageData.h"

void setup() {
    DEV_Module_Init();
    printf("EPD_9IN7E_test Demo\r\n");

    printf("e-Paper Init and Clear...\r\n");
    EPD_9IN7E_Init();
    //EPD_9IN7E_Clear(EPD_9IN7E_WHITE);
    DEV_Delay_ms(2000);

    //Create a new image cache
    UBYTE *Image;
    UDOUBLE Imagesize = ((EPD_9IN7E_WIDTH % 2 == 0)? (EPD_9IN7E_WIDTH / 2 ): (EPD_9IN7E_WIDTH / 2 + 1)) * EPD_9IN7E_HEIGHT;
    if((Image = (UBYTE *)malloc(Imagesize)) == NULL) {
        printf("Failed to apply for black memory...\r\n");
    }

    printf("Paint_NewImage\r\n");
    Paint_NewImage(Image, EPD_9IN7E_WIDTH, EPD_9IN7E_HEIGHT, 0, WHITE);
    Paint_SetScale(6);

#if 1   // Show the built-in image first; this does not need a RAM framebuffer.
    printf("show bmp--------------\r\n");
    EPD_9IN7E_Display(Image6color1);
    DEV_Delay_ms(3000);
#endif

#if 1   // Drawing on the image
    Paint_NewImage(Image, EPD_9IN7E_WIDTH, EPD_9IN7E_HEIGHT, 0, EPD_9IN7E_WHITE);
    Paint_SetScale(6);
    // 1.Select Image
    printf("SelectImage:BlackImage\r\n");
    Paint_SelectImage(Image);
    Paint_Clear(EPD_9IN7E_WHITE);

    // 2.Drawing on the image
    printf("Drawing:BlackImage\r\n");
    Paint_DrawPoint(10, 80, EPD_9IN7E_RED, DOT_PIXEL_1X1, DOT_STYLE_DFT);
    Paint_DrawPoint(10, 90, EPD_9IN7E_BLUE, DOT_PIXEL_2X2, DOT_STYLE_DFT);
    Paint_DrawPoint(10, 100, EPD_9IN7E_GREEN, DOT_PIXEL_3X3, DOT_STYLE_DFT);
    Paint_DrawLine(20, 70, 70, 120, EPD_9IN7E_YELLOW, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
    Paint_DrawLine(70, 70, 20, 120, EPD_9IN7E_YELLOW, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
    Paint_DrawRectangle(20, 70, 70, 120, EPD_9IN7E_BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawRectangle(80, 70, 130, 120, EPD_9IN7E_BLACK, DOT_PIXEL_1X1, DRAW_FILL_FULL);
    Paint_DrawCircle(45, 95, 20, EPD_9IN7E_BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(105, 95, 20, EPD_9IN7E_WHITE, DOT_PIXEL_1X1, DRAW_FILL_FULL);
    Paint_DrawLine(85, 95, 125, 95, EPD_9IN7E_YELLOW, DOT_PIXEL_1X1, LINE_STYLE_DOTTED);
    Paint_DrawLine(105, 75, 105, 115, EPD_9IN7E_YELLOW, DOT_PIXEL_1X1, LINE_STYLE_DOTTED);
    Paint_DrawString_CN(10, 120, "你好abc", &Font12CN, EPD_9IN7E_BLACK, EPD_9IN7E_WHITE);
    Paint_DrawString_CN(10, 140, "微雪电子", &Font24CN, EPD_9IN7E_WHITE, EPD_9IN7E_BLACK);
    Paint_DrawNum(10, 33, 123456789, &Font12, EPD_9IN7E_BLACK, EPD_9IN7E_WHITE);
    Paint_DrawNum(10, 50, 987654321, &Font16, EPD_9IN7E_WHITE, EPD_9IN7E_BLACK);
    Paint_DrawString_EN(400, 0, "waveshare", &Font16, EPD_9IN7E_BLACK, EPD_9IN7E_WHITE);
    Paint_DrawString_EN(400, 20, "waveshare", &Font16, EPD_9IN7E_GREEN, EPD_9IN7E_WHITE);
    Paint_DrawString_EN(400, 40, "waveshare", &Font16, EPD_9IN7E_BLUE, EPD_9IN7E_WHITE);
    Paint_DrawString_EN(400, 60, "waveshare", &Font16, EPD_9IN7E_RED, EPD_9IN7E_WHITE);
    Paint_DrawString_EN(400, 80, "waveshare", &Font16, EPD_9IN7E_YELLOW, EPD_9IN7E_WHITE);
    Paint_DrawString_EN(400, 100, "waveshare", &Font16, EPD_9IN7E_WHITE, EPD_9IN7E_BLACK);
    Paint_DrawString_EN(150, 0, "hello world", &Font24, EPD_9IN7E_WHITE, EPD_9IN7E_BLACK);
    Paint_DrawString_EN(150, 30, "hello world", &Font24, EPD_9IN7E_GREEN, EPD_9IN7E_BLACK);
    Paint_DrawString_EN(150, 60, "hello world", &Font24, EPD_9IN7E_BLUE, EPD_9IN7E_BLACK);
    Paint_DrawString_EN(150, 90, "hello world", &Font24, EPD_9IN7E_RED, EPD_9IN7E_BLACK);
    Paint_DrawString_EN(150, 120, "hello world", &Font24, EPD_9IN7E_YELLOW, EPD_9IN7E_BLACK);
    Paint_DrawString_EN(150, 150, "hello world", &Font24, EPD_9IN7E_BLACK, EPD_9IN7E_WHITE);

    printf("EPD_Display\r\n");
    EPD_9IN7E_Display(Image);
    DEV_Delay_ms(3000);
#endif

    printf("Clear...\r\n");
    EPD_9IN7E_Init();
    EPD_9IN7E_Clear(EPD_9IN7E_WHITE);
    DEV_Delay_ms(500);
    EPD_9IN7E_Sleep();
    free(Image);
    Image = NULL;
    DEV_Delay_ms(2000);
    // close 5V
    printf("close 5V, Module enters 0 power consumption ...\r\n");
    DEV_Module_Exit();

}

void loop() {
  

}
