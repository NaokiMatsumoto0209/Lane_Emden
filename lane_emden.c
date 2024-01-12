//
// lane_emden.case
//
// created by Naoki Matsumoto on 2021/11/19.
//
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/*----lane_emdenの定義----*/
double dvdr(double d, double v, double r, double g){ //二階微分の式
  return -pow(d, g)-2.0*v/r;
}

double dddr(double d, double v, double r, double g){ //一回微分の式 = vとしている
  return v;
}
/*----lane_emdenの定義----*/

/*====main関数====*/
int main(int argc, char *argv[]) { //実行時の引数として、「出力ファイル名」と「パラメータ」を入力
  const double g = atof( argv[2] ); //パラメータの定義
  //double型で入力

  /*----ファイルポインタ----*/
  FILE *fp;
  /*----ファイルポインタ----*/

  const int n = 2e9; //forループの打ち切り回数
  const double rmax = 20.0; //計算の打ち切りの半径の値
  double dr = rmax/(double)n; //計算の刻み幅

  /*----初期条件の設定----*/
  double r = dr; //初期で半径0.0 -> 刻み幅dr
  double d = 1.0 - dr*dr/6.0 + g*dr*dr*dr*dr/120.0; //初期で密度比1.0 -> 近似の\xiのあたい
  double v = - dr/3.0 + g*dr*dr*dr/30.0; //初期で密度比変化0.0 -> 近似のd\xi/d
  /*----初期条件の設定----*/

  //double m = 0.0; //全質量の計算

  /*----出力ファイルの指定----*/
  fp = fopen( argv[1], "r" );
  //指定したファイルをreadモードで開き、

  if( fp != NULL ){
    printf( "Error!!: This file already exists.\n" );
    fclose( fp );
    return 1; //すでに内容が存在するならば終了
  }
  fclose( fp );
  fp = fopen( argv[1], "w" ); //改めてwriteモードで開く
  /*----出力ファイルの指定----*/

  fprintf(fp, "#i\tr\tv\td\n" );

  double r1 = 0.0; //記録用の変数

  for ( int i = 1; i < n; ++i ){
    double kr = r + 0.5 * dr;

    double kd1 = dddr(d, v, r, g);
    double kv1 = dvdr(d, v, r, g);

    double kd2 = dddr(d + 0.5*dr*kd1, v + 0.5*dr*kv1, kr, g);
    double kv2 = dvdr(d + 0.5*dr*kd1, v + 0.5*dr*kv1, kr, g);

    double kd3 = dddr(d + 0.5*dr*kd2, v + 0.5*dr*kv2, kr, g);
    double kv3 = dvdr(d + 0.5*dr*kd2, v + 0.5*dr*kv2, kr, g);

    double kd4 = dddr(d + dr*kd3, v + dr*kv3, r + dr, g);
    double kv4 = dvdr(d + dr*kd3, v + dr*kv3, r + dr, g);

    d += dr*(kd1 + 2.0*kd2 + 2.0*kd3 + kd4)/6.0;
    v += dr*(kv1 + 2.0*kv2 + 2.0*kv3 + kv4)/6.0;
    r += dr;

    /*
    if ( d < 0.0 ){
      printf("半径は %.16g、bar{rho}/rho_cは %.16g、 打ち切り回数は %d\n", r1, -r1/3.0/v, i);
      fclose(fp);
      return 0; //密度が負というのは非物理的なので、計算を止める
    }*/
    r1 = r;
    if (i % 1000 == 0){
      printf("%d\t %lf\t %lf\t %lf\n", i, r, v, d );
      fprintf(fp, "%d\t %.8g\t %.8g\t %.8g\n", i, r1, v, d );
    }
  }

  printf("半径は %.8g、bar{rho}/rho_cは %.8g、 打ち切り回数は %d\n", r1, - r1/3.0/v, n);
  fclose(fp);
  return 0;
}
/*====main関数====*/
