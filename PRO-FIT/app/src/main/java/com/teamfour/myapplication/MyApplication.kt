package com.teamfour.myapplication

import android.app.Application
import android.content.Context

class MyApplication: Application() {

    companion object{
        lateinit var instance: MyApplication
        fun ApplicationContext(): Context {
            return instance.applicationContext
        }
    }

    init{
        instance = this
    }
}