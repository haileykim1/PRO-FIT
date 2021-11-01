package com.teamfour.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.view.Window
import com.teamfour.myapplication.databinding.ActivitySplashBinding

class SplashActivity : BaseActivity() {

    val binding by lazy {ActivitySplashBinding.inflate(layoutInflater)}

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
        //GlobalContext.setContext(this)

        //2초동안 기다렸다가 정보 입력 여부에 따라 다음 액티비티로 넘어감
        Handler().postDelayed({
            val intent: Intent = if(false) {
            Intent(this, MainActivity::class.java)
            }else{
                Intent(this, InitInfoActivity::class.java)
            }
            startActivity(intent)
            finish()
        }, 2000)

        //UserInfo.has(UserInfo.NAME_PASSED) && UserInfo.get(UserInfo.NAME_PASSED) == true
    }
}
